import datetime
from decimal import Decimal

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

PAREIGOS = (
    ('ATSAKINGAS ASMUO', 'Atsakingas asmuo'),
    ('KOMISIJOS NARYS PIRMININKAS', 'Komisijos narys pirmininkas'),
    ('KOMISIJOS NARYS', 'Komisijos narys'),
    ('DIREKTORIUS', 'Direktorius'),
    ('ADMIN', 'Admin'),
)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)

    vardas = models.CharField(max_length = 100, default = None, null = True, blank = True)
    pavarde = models.CharField(max_length = 100, default = None, null = True, blank = True)
    pareigos = models.CharField(max_length = 100, default = 'ADMIN', choices = PAREIGOS, null = True, blank = False)
    darbo_istaiga = models.CharField(max_length = 100, default = None, null = True, blank = True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender = User)
def create_profile(sender, instance, created, **kwargs):
    if created:  
       UserProfile.objects.create(user = instance) 

@receiver(post_save, sender = User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()

class PVMSask(models.Model):
    serija = models.CharField(max_length = 3, default = '123', unique = True)
    nr = models.CharField(max_length = 3, default = 'AAA') 
    data = models.DateField(default = datetime.date.today)
    
    pirkejas = models.CharField(max_length = 100, default = 'Petras Petraitis')
    pirkejo_adresas = models.CharField(max_length = 100, default = 'Pievu g. 7-18')
    pirkejo_asmens_kodas = models.CharField(max_length = 100, default = '39612656985')
    pirkejo_PVM_moketojo_kodas = models.CharField(max_length = 100, default = '8541224566')

    pardavejas = models.CharField(max_length = 100, default = 'Jonas Jonaitis')
    pardavejo_adresas = models.CharField(max_length = 100, default = 'Gargzdu pr. 8-127')
    pardavejo_asmens_kodas = models.CharField(max_length = 100, default = '39656237415')
    pardavejo_PVM_moketojo_kodas = models.CharField(max_length = 100, default = '8541224566')
    
    israses_asmuo = models.ForeignKey(User, blank = True, null = True)

    def __str__(self):
        return ' '.join(['Serija', self.serija, 'Nr.', self.nr,])

class NurasymoAktas(models.Model):
    is_submited = models.BooleanField(default = False)

    data = models.DateField(default = datetime.date.today)
    nr = models.CharField(max_length = 100, default = None)
    viso_suma = models.DecimalField(default = None, null = True, blank = True, max_digits = 12, decimal_places = 2)
    
    PVM_saskaitos = models.ManyToManyField(PVMSask, default = None, related_name = 'nurasymo_aktai')

    atsakingas_asmuo = models.ForeignKey(User, blank = True, null = True, related_name = 'atsakingas_asmuo')
    patvirtines_direktorius = models.ForeignKey(User, blank = True, null = True, related_name = 'patvirtines_direktorius')
    komisijos_pirmininkas = models.ForeignKey(User, blank = True, null = True, related_name = 'komisijos_pirmininkas')

    def __str__(self):
        return self.nr

class NurasymoAktoIrasas(models.Model):
    nurasymo_aktas = models.ForeignKey(NurasymoAktas, default = None, on_delete = models.CASCADE, blank = True,
                                       null = True)
    PVM_iraso_pk = models.IntegerField(default = None, blank = True, null = True)

    mat_vertybes_pav = models.CharField(max_length = 100, default = None, blank = True, null = True)
    mato_vnt = models.CharField(max_length = 100, default = None, blank = True, null = True)
    kiekis = models.IntegerField(default = None, blank = True, null = True)
    kaina = models.DecimalField(default = None, blank = True, null = True, max_digits = 12, decimal_places = 2)
    suma_su_PVM = models.DecimalField(default = None, blank = True, null = True, max_digits = 12, decimal_places = 2)
    panaudojimo_tikslas = models.CharField(max_length = 100, default = None, blank = True, null = True)

    max_kiekis = models.IntegerField(default = None, blank = True, null = True)
    israses_komisijos_narys = models.ForeignKey(User, blank = True, null = True)
    
    def save(self, *args, **kwargs):
        self.suma_su_PVM = round((self.kaina * self.kiekis),2)
        super(NurasymoAktoIrasas, self).save(*args, **kwargs)
        
    def __str__(self):
        return ' '.join([self.mat_vertybes_pav, str(self.kiekis)])

class PVMIrasas(models.Model):
    iraso_nr = models.AutoField(primary_key = True)

    prekes_pavadinimas = models.CharField(max_length = 100, default = 'bananas')
    matavimo_vnt = models.CharField(max_length = 100, default = 'vnt')
    kiekis = models.IntegerField(default = 8)
    vnt_kaina_be_PVM = models.DecimalField(default = Decimal('5.00'), max_digits = 12, decimal_places = 2)
    PVM_tarifas = models.IntegerField(default = 21)

    suma_be_PVM = models.DecimalField(default = None, max_digits = 12, decimal_places = 2)
    PVM_suma = models.DecimalField(default = None, max_digits = 12, decimal_places = 2)
    suma_viso = models.DecimalField(default = None, max_digits = 12, decimal_places = 2)

    PVM_saskaita = models.ForeignKey(PVMSask, default = None, blank = True, null = True, on_delete = models.CASCADE)
    nurasymo_aktas = models.ForeignKey(NurasymoAktas, null = True, blank = True, default = None,
                                       on_delete = models.SET_NULL)

    @property
    def get_suma_be_PVM(self):
        return self.kiekis * self.vnt_kaina_be_PVM

    @property
    def get_PVM_suma(self):
        return self.get_suma_be_PVM / 100 * self.PVM_tarifas

    @property
    def get_suma_viso(self):
        return self.get_PVM_suma + self.get_suma_be_PVM

    def save(self, *args, **kwargs):
        self.suma_be_PVM = self.get_suma_be_PVM
        self.PVM_suma = self.get_PVM_suma
        self.suma_viso = self.get_suma_viso
        super(PVMIrasas, self).save(*args, **kwargs)

    def __str__(self):
        return self.prekes_pavadinimas + " " + str(self.iraso_nr)


