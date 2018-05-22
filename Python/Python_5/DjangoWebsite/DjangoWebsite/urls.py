from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

import app.forms
import app.views
from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^$', app.views.home, name='home'),
    url(r'^saskaita', app.views.SaskaitaView.as_view(), name='saskaita'),
    url(r'^duomenys', app.views.DuomenysView.as_view(), name='duomenys'),
    url(r'^nurasymas', app.views.NurasymasView.as_view(), name='nurasymas'),
    url(r'^ruosiniai', app.views.RuosiniaiView.as_view(), name='ruosiniai'),
    url(r'^account', app.views.AccountView.as_view(), name='account'),
    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'app/login.html',
            'authentication_form': app.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'PVM saskaitu tvarkymo sistema',
                'year': datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),

    url(r'^admin/', include(admin.site.urls))
]
