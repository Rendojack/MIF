from django.contrib.auth.decorators import login_required
from django.forms.formsets import formset_factory
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView

from app.forms import IrasasForm
from app.forms import IrasasMultipleSelectForm
from app.forms import NurasymasForm
from app.forms import NurasymoAktasMultipleSelectForm
from app.forms import NurasymoAktoPasirinkimoForm
from app.forms import NurasymoAktoPasirinkimoFormSuCharField
from app.forms import NurasymoIrasasForm
from app.forms import PVMIrasuPasirinkimoForm
from app.forms import PVMSaskPasirinkimoFormRadio
from app.forms import SaskaitaForm
from app.forms import SaskaitaMultipleSelectForm
from app.models import NurasymoAktas
from app.models import NurasymoAktoIrasas
from app.models import PVMIrasas
from app.models import PVMSask

from app.pdf_renderer import Render


def home(request):
    assert isinstance(request, HttpRequest)
    return render(request, 'app/index.html')

@method_decorator(login_required, name = 'get')
@method_decorator(login_required, name = 'post')
class SaskaitaView(TemplateView):
    template_name = 'app/saskaita.html'

    def get(self, request):
        form = SaskaitaForm()
        form_irasas = IrasasForm()

        submits = PVMSask.objects.all().order_by('data')
        
        args = {'form': form, 'form_irasas': form_irasas, 'submits': submits}
        return render(request, self.template_name, args)

    def post(self, request):
        if 'btn_forma' in request.POST:
            form = SaskaitaForm(request.POST)
            if form.is_valid():
                submit = form.save(commit = False)
                submit.israses_asmuo = request.user
                submit.save()

                return redirect('saskaita')

        if 'btn_irasas' in request.POST:
            form = IrasasForm(request.POST)
            if form.is_valid():
                submit = form.save(commit = False)
                submit.save()

                return redirect('saskaita')

        form = SaskaitaForm()
        form_irasas = IrasasForm()
        submits = PVMSask.objects.all().order_by('data')

        args = {'form': form, 'form_irasas': form_irasas, 'submits': submits}
        return render(request, self.template_name, args)

@method_decorator(login_required, name = 'get')
@method_decorator(login_required, name = 'post')
class DuomenysView(TemplateView):
    template_name = 'app/duomenys.html'

    def get(self, request):
        sask_radio_form = SaskaitaMultipleSelectForm()
        irasas_radio_form = IrasasMultipleSelectForm()
        nurasymo_aktai_radio_form = NurasymoAktasMultipleSelectForm()

        PVM_saskaitos = PVMSask.objects.all()
        PVM_irasai = PVMIrasas.objects.all().order_by('PVM_saskaita')
        
        nurasymo_irasai = NurasymoAktoIrasas.objects.all()
        nurasymo_aktai = NurasymoAktas.objects.all()

        args = {'sask_radio_form': sask_radio_form, 
                'irasas_radio_form': irasas_radio_form,
                'nurasymo_aktai_radio_form': nurasymo_aktai_radio_form,
                'PVM_saskaitos': PVM_saskaitos, 
                'PVM_irasai': PVM_irasai, 
                'nurasymo_irasai': nurasymo_irasai,
                'nurasymo_aktai': nurasymo_aktai}

        return render(request, self.template_name, args)

    def post(self, request):
        if 'btn_sask_del' in request.POST:
            form = SaskaitaMultipleSelectForm(request.POST)
            if form.is_valid():
                ids_to_del = request.POST.getlist('selections')
                for id_to_del in ids_to_del:
                    PVMSask.objects.get(pk = id_to_del).delete()

        if 'btn_irasas_del' in request.POST:
            form = IrasasMultipleSelectForm(request.POST)
            if form.is_valid():
                ids_to_del = request.POST.getlist('selections')
                for id_to_del in ids_to_del:
                    PVMIrasas.objects.get(pk = id_to_del).delete()

        if 'btn_nurasymo_aktas_del' in request.POST:
            form = NurasymoAktasMultipleSelectForm(request.POST)
            if form.is_valid():
                ids_to_del = request.POST.getlist('selections')
                for id_to_del in ids_to_del:
                    NurasymoAktas.objects.get(pk = id_to_del).delete()

        return redirect('duomenys')

@method_decorator(login_required, name = 'get')
@method_decorator(login_required, name = 'post')
class NurasymasView(TemplateView):
    template_name = 'app/nurasymas.html'

    def get(self, request):

        nurasymo_aktas_form = NurasymasForm()
        nurasymo_irasas_form = NurasymoIrasasForm()

        aktai = NurasymoAktas.objects.filter(is_submited = True)  
        nurasymo_akto_pasirinkimo_form = NurasymoAktoPasirinkimoForm()

        show_btn_kurti_nurasymo_akta = True
        show_btn_pasirinkti_nurasymo_akta = True
        show_btn_pasirinkti_PVM_irasus = False
        show_btn_nurasyti = False

        args = {'nurasymo_aktas_form': nurasymo_aktas_form,
                'nurasymo_irasas_form': nurasymo_irasas_form,
                'nurasymo_akto_pasirinkimo_form': nurasymo_akto_pasirinkimo_form,
                'show_btn_kurti_nurasymo_akta': show_btn_kurti_nurasymo_akta,
                'show_btn_pasirinkti_nurasymo_akta': show_btn_pasirinkti_nurasymo_akta,
                'show_btn_pasirinkti_PVM_irasus': show_btn_pasirinkti_PVM_irasus,
                'show_btn_nurasyti': show_btn_nurasyti}

        return render(request, self.template_name, args)

    def post(self, request):
        nurasymo_aktas_form = NurasymasForm(request.POST)
        nurasymo_irasas_form = NurasymoIrasasForm(request.POST)
        nurasymo_akto_pasirinkimo_form = NurasymoAktoPasirinkimoForm(request.POST)
        PVM_irasu_pasirinkimo_form = PVMIrasuPasirinkimoForm(request.POST)

        NurasymoFormSet = formset_factory(NurasymoIrasasForm)
        nurasymo_irasu_formset = NurasymoFormSet(request.POST, request.FILES)

        if 'btn_kurti_nurasymo_akta' in request.POST and nurasymo_aktas_form.is_valid():

                submit = nurasymo_aktas_form.save(commit = False)
                submit.atsakingas_asmuo = request.user
                submit.save()
                nurasymo_aktas_form.save_m2m()

                return redirect('nurasymas')

        if 'btn_pasirinkti_nurasymo_akta' in request.POST and nurasymo_akto_pasirinkimo_form.is_valid():

            nurasymo_akto_pk = request.POST.get('selection')
            nurasymo_aktas = NurasymoAktas.objects.get(pk=nurasymo_akto_pk)
            nurasymo_akto_saskaitos = nurasymo_aktas.PVM_saskaitos.all()

            irasu_formos = []
            PVM_irasai = PVMIrasas.objects.none()

            for nurasymo_akto_saskaita in nurasymo_akto_saskaitos:
                for PVM_irasas in nurasymo_akto_saskaita.pvmirasas_set.all():
                        setattr(PVM_irasas, 'nurasymo_aktas', nurasymo_aktas)
                        PVM_irasas.save()

                # apjungiam n querysetu i viena queryseta
                PVM_irasai = PVM_irasai | nurasymo_akto_saskaita.pvmirasas_set.all()

            PVM_irasu_pasirinkimo_form = PVMIrasuPasirinkimoForm(queryset = PVM_irasai)

            show_btn_kurti_nurasymo_akta = False
            show_btn_pasirinkti_nurasymo_akta = False
            show_btn_pasirinkti_PVM_irasus = True
            show_btn_nurasyti = False

            args = {'PVM_irasu_pasirinkimo_form': PVM_irasu_pasirinkimo_form,
                    'show_btn_kurti_nurasymo_akta': show_btn_kurti_nurasymo_akta,
                    'show_btn_pasirinkti_nurasymo_akta': show_btn_pasirinkti_nurasymo_akta,
                    'show_btn_pasirinkti_PVM_irasus': show_btn_pasirinkti_PVM_irasus,
                    'show_btn_nurasyti': show_btn_nurasyti}

            return render(request, self.template_name, args)

        if 'btn_pateikti_nurasymo_akta' in request.POST and nurasymo_akto_pasirinkimo_form.is_valid():

            nurasymo_akto_pk = request.POST.get('selection')
            nurasymo_aktas = NurasymoAktas.objects.get(pk=nurasymo_akto_pk)
            setattr(nurasymo_aktas, 'is_submited', True) 
            setattr(nurasymo_aktas, 'komisijos_pirmininkas', request.user) 
            nurasymo_aktas.save()

            return redirect('nurasymas')

        if 'btn_pasirinkti_PVM_irasus' in request.POST and PVM_irasu_pasirinkimo_form.is_valid():

            pasirinktu_PVM_irasu_pks = request.POST.getlist('PVM_irasai')
            pasirinkti_PVM_irasai = []

            for pasirinkto_PVM_iraso_pk in pasirinktu_PVM_irasu_pks:
                pasirinkti_PVM_irasai.append(PVMIrasas.objects.get(pk = pasirinkto_PVM_iraso_pk))
            
            nurasymo_irasu_formos = []

            nurasymo_akto_irasai = NurasymoAktoIrasas.objects.all()

            list_of_dictionaries = []
            list_of_instances = []

            for pasirinktas_PVM_irasas in pasirinkti_PVM_irasai:
                dictionary = {}
                if(len(nurasymo_akto_irasai) > 0):
                    for index, nurasymo_akto_irasas in enumerate(nurasymo_akto_irasai):
                        # jei egzistuoja toks irasas - paruosiam UPDATE'ui
                        if(pasirinktas_PVM_irasas.pk == nurasymo_akto_irasas.PVM_iraso_pk and
                                nurasymo_akto_irasas.nurasymo_aktas == pasirinktas_PVM_irasas.nurasymo_aktas):
                            nurasymo_irasas = \
                                NurasymoAktoIrasas.objects.get(PVM_iraso_pk = pasirinktas_PVM_irasas.pk,
                                                                nurasymo_aktas = pasirinktas_PVM_irasas.nurasymo_aktas)

                            dictionary['PVM_iraso_pk'] = nurasymo_akto_irasas.PVM_iraso_pk
                            dictionary['nurasymo_aktas'] = nurasymo_irasas.nurasymo_aktas
                            dictionary['mat_vertybes_pav'] = nurasymo_irasas.mat_vertybes_pav
                            dictionary['mato_vnt'] = nurasymo_irasas.mato_vnt
                            dictionary['kaina'] = nurasymo_irasas.kaina
                            dictionary['kiekis'] = nurasymo_irasas.kiekis
                            dictionary['panaudojimo_tikslas'] = nurasymo_irasas.panaudojimo_tikslas
                            dictionary['max_kiekis'] = nurasymo_irasas.max_kiekis

                            list_of_dictionaries.append(dictionary)
                            nurasymo_irasas.delete() # istrinam sena irasa, kad nebutu 2 vienodu
                            break;

                        # jei neegzistuoja - paruosiam NAUJA irasa
                        elif(index == len(nurasymo_akto_irasai) - 1):# last index
                            dictionary['PVM_iraso_pk'] = pasirinktas_PVM_irasas.pk
                            dictionary['nurasymo_aktas'] = pasirinktas_PVM_irasas.nurasymo_aktas
                            dictionary['mat_vertybes_pav'] = pasirinktas_PVM_irasas.prekes_pavadinimas
                            dictionary['mato_vnt'] = pasirinktas_PVM_irasas.matavimo_vnt
                            dictionary['kaina'] = round((pasirinktas_PVM_irasas.vnt_kaina_be_PVM +
                                                         (pasirinktas_PVM_irasas.vnt_kaina_be_PVM / 100 *
                                                          pasirinktas_PVM_irasas.PVM_tarifas)), 2)
                            dictionary['max_kiekis'] = pasirinktas_PVM_irasas.kiekis

                            list_of_dictionaries.append(dictionary)
                else:
                        dictionary['PVM_iraso_pk'] = pasirinktas_PVM_irasas.pk
                        dictionary['nurasymo_aktas'] = pasirinktas_PVM_irasas.nurasymo_aktas
                        dictionary['mat_vertybes_pav'] = pasirinktas_PVM_irasas.prekes_pavadinimas
                        dictionary['mato_vnt'] = pasirinktas_PVM_irasas.matavimo_vnt
                        dictionary['kaina'] = round((pasirinktas_PVM_irasas.vnt_kaina_be_PVM +
                                                     (pasirinktas_PVM_irasas.vnt_kaina_be_PVM / 100 *
                                                      pasirinktas_PVM_irasas.PVM_tarifas)), 2)
                        dictionary['max_kiekis'] = pasirinktas_PVM_irasas.kiekis

                        list_of_dictionaries.append(dictionary)

            show_btn_kurti_nurasymo_akta = False
            show_btn_pasirinkti_nurasymo_akta = False
            show_btn_pasirinkti_PVM_irasus = False
            show_btn_nurasyti = True

            NurasymoFormSet = formset_factory(NurasymoIrasasForm, min_num = len(pasirinkti_PVM_irasai),
                                                                    max_num = len(pasirinkti_PVM_irasai))
            formset = NurasymoFormSet(initial = list_of_dictionaries)

            args = {'PVM_irasu_pasirinkimo_form': PVM_irasu_pasirinkimo_form,
                    'show_btn_kurti_nurasymo_akta': show_btn_kurti_nurasymo_akta,
                    'show_btn_pasirinkti_nurasymo_akta': show_btn_pasirinkti_nurasymo_akta,
                    'show_btn_pasirinkti_PVM_irasus': show_btn_pasirinkti_PVM_irasus,
                    'formset': formset,
                    'show_btn_nurasyti': show_btn_nurasyti}

            return render(request, self.template_name, args)

        if 'btn_nurasyti' in request.POST and nurasymo_irasu_formset.is_valid():

            nurasymo_akto_pk = nurasymo_irasu_formset[0]['nurasymo_aktas'].value()
            nurasymo_aktas = NurasymoAktas.objects.get(pk=nurasymo_akto_pk) 

            for form in nurasymo_irasu_formset.forms:
                submit = form.save(commit = False)
                if submit.kiekis > submit.max_kiekis:
                    continue
                else:     
                    submit.israses_komisijos_narys = request.user
                    submit.save()

            viso_suma = 0
            for nurasymo_irasas in nurasymo_aktas.nurasymoaktoirasas_set.all():
                viso_suma = viso_suma + nurasymo_irasas.suma_su_PVM

            setattr(nurasymo_aktas, 'viso_suma', viso_suma)
            nurasymo_aktas.save()
                        
            return redirect('nurasymas')

        return redirect('nurasymas')

@method_decorator(login_required, name = 'get')
@method_decorator(login_required, name = 'post')
class RuosiniaiView(TemplateView):
    template_name = 'app/ruosiniai.html'

    def get(self, request):
        aktai = NurasymoAktas.objects.filter(is_submited = True) 
        nurasymo_akto_pasirinkimo_form = NurasymoAktoPasirinkimoFormSuCharField(queryset = aktai)
        PVM_sask_pasirinkimo_form_radio = PVMSaskPasirinkimoFormRadio()

        args = {'nurasymo_akto_pasirinkimo_form': nurasymo_akto_pasirinkimo_form,
                'PVM_sask_pasirinkimo_form_radio': PVM_sask_pasirinkimo_form_radio}

        return render(request, self.template_name, args)

    def post(self, request):
        nurasymo_akto_pasirinkimo_form = NurasymoAktoPasirinkimoFormSuCharField(request.POST)
        PVM_sask_pasirinkimo_form_radio = PVMSaskPasirinkimoFormRadio(request.POST)

        if 'btn_generuoti_nurasyma' in request.POST:
            try:
                nurasymo_aktas_rodyti = NurasymoAktas.objects.get(pk = request.POST.get('selection'))
                nurasymo_irasai = NurasymoAktoIrasas.objects.filter(nurasymo_aktas = nurasymo_aktas_rodyti)
                susijusios_PVM_sask = nurasymo_aktas_rodyti.PVM_saskaitos.all()

                komisijos_nariai = []

                for nurasymo_irasas in nurasymo_irasai:
                    if(nurasymo_irasas.israses_komisijos_narys.userprofile.pareigos != 'KOMISIJOS NARYS PIRMININKAS') \
                            and not nurasymo_irasas.israses_komisijos_narys in komisijos_nariai:
                        komisijos_nariai.append(nurasymo_irasas.israses_komisijos_narys)

                komisijos_pirmininkas = nurasymo_aktas_rodyti.komisijos_pirmininkas

                isakymo_nr = request.POST.get('isakymo_nr')
                isakymo_nr = isakymo_nr.strip()
                if not isakymo_nr:
                    raise Exception

                args = {'nurasymo_akto_pasirinkimo_form': nurasymo_akto_pasirinkimo_form,
                        'nurasymo_aktas_rodyti': nurasymo_aktas_rodyti,
                        'nurasymo_irasai': nurasymo_irasai,
                        'susijusios_PVM_sask': susijusios_PVM_sask,
                        'komisijos_nariai': komisijos_nariai,
                        'komisijos_pirmininkas': komisijos_pirmininkas,
                        'direktorius': request.user,
                        'isakymo_nr': isakymo_nr}

                return Render.render_to_pdf('app/pdf/pdf-nurasymas.html', args)

            except Exception as e:
                print(str(e))
                return redirect('ruosiniai')

        elif 'btn_generuoti_PVM' in request.POST:
            try:
                PVM_sask = PVMSask.objects.get(pk = request.POST.get('saskaitos'))
                PVM_irasai = list(PVM_sask.pvmirasas_set.all())

                prekiu_suma_viso = 0
                for PVM_irasas in PVM_irasai:
                    prekiu_suma_viso = prekiu_suma_viso + PVM_irasas.suma_viso
                
                args = {'PVM_sask': PVM_sask,
                        'PVM_irasai': PVM_irasai,
                        'prekiu_suma_viso': prekiu_suma_viso}

                return Render.render_to_pdf('app/pdf/pdf-sask.html', args)

            except Exception as e:
                print(str(e))
                return redirect('ruosiniai')

        return redirect('paruosti')

@method_decorator(login_required, name = 'get')
class AccountView(TemplateView):
    template_name = 'app/account.html'

    def get(self, request):

        args = {'user_profile': request.user.userprofile,
                'user': request.user}
        return render(request, self.template_name, args)