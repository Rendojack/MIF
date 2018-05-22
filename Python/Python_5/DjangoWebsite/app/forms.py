from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _

from app.models import NurasymoAktas
from app.models import NurasymoAktoIrasas
from app.models import PVMIrasas
from app.models import PVMSask

class BootstrapAuthenticationForm(AuthenticationForm):
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

class SaskaitaForm(forms.ModelForm):
    class Meta:
        model = PVMSask
        fields =  '__all__' 

class IrasasForm(forms.ModelForm):
    class Meta:
        model = PVMIrasas
        fields = ['prekes_pavadinimas',
                  'matavimo_vnt',
                  'kiekis',
                  'vnt_kaina_be_PVM',
                  'PVM_tarifas',
                  'PVM_saskaita']

class NurasymasForm(forms.ModelForm):
    class Meta:
        model = NurasymoAktas
        exclude = ('viso_suma', 'is_submited',)

class NurasymoAktoPasirinkimoForm(forms.Form):
    selection = forms.ModelChoiceField(queryset = NurasymoAktas.objects.filter(is_submited = False),
                                       widget = forms.RadioSelect,
                                       empty_label = None)

    def __init__(self, *args, **kwargs):
            qs = kwargs.pop("queryset", None)
            super(NurasymoAktoPasirinkimoForm, self).__init__(*args, **kwargs)
            if qs is not None:
                self.fields['selection'].queryset = qs

class NurasymoAktoPasirinkimoFormSuCharField(forms.Form):
    selection = forms.ModelChoiceField(queryset = NurasymoAktas.objects.filter(is_submited = False),
                                       widget = forms.RadioSelect,
                                       empty_label = None)
    isakymo_nr = forms.CharField(max_length = 100)

    def __init__(self, *args, **kwargs):
            qs = kwargs.pop("queryset", None)
            super(NurasymoAktoPasirinkimoFormSuCharField, self).__init__(*args, **kwargs)
            if qs is not None:
                self.fields['selection'].queryset = qs

class PVMSaskPasirinkimoFormRadio(forms.Form):
    saskaitos = forms.ModelMultipleChoiceField(queryset = PVMSask.objects.all(),
                                                widget = forms.RadioSelect)

class PVMIrasuPasirinkimoForm(forms.Form):
    PVM_irasai = forms.ModelMultipleChoiceField(queryset = PVMIrasas.objects.all(),
                                                widget = forms.CheckboxSelectMultiple)
    def __init__(self, *args, **kwargs):
            qs = kwargs.pop("queryset", None)
            super(PVMIrasuPasirinkimoForm, self).__init__(*args, **kwargs)
            if qs is not None:
                self.fields['PVM_irasai'].queryset = qs

class NurasymoIrasasForm(forms.ModelForm):
    class Meta:
        model = NurasymoAktoIrasas
        exclude = ('suma_su_PVM',
                   'israses_komisijos_narys',)

class SaskaitaMultipleSelectForm(forms.Form):
    selections = forms.ModelMultipleChoiceField(queryset = PVMSask.objects.all(), 
                                                widget = forms.SelectMultiple)

class IrasasMultipleSelectForm(forms.Form):
    selections = forms.ModelMultipleChoiceField(queryset = PVMIrasas.objects.all(), 
                                                widget = forms.SelectMultiple)

class NurasymoAktasMultipleSelectForm(forms.Form):
    selections = forms.ModelMultipleChoiceField(queryset = NurasymoAktas.objects.all(), 
                                                widget = forms.SelectMultiple)
