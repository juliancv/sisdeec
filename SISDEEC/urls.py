"""SISDEEC URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from usuarios.views import *
from solicitudes.views import *
from django.contrib.auth import views as auth_views

urlpatterns_usuarios = [
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='auth_logout'),
    url(r'nuevo/$', PersonaCreateView.as_view(), name = 'nuevo_usuario'),
    url(r'^detalles/$', PersonaDetalles.as_view(), name = 'detalles'),
    url(r'^editar/$', PersonaEditar.as_view(), name = 'editar'),
    url(r'lista_usuarios/$', ListarUsuarios.as_view(), name = 'lista_usuarios'),
    url(r'/$', Home.as_view(), name = 'home'),

]

urlpatterns_solicitudes = [
    url(r'nueva_solicitud/$', ActividadCreateView.as_view(), name = 'nueva_solicitud'),
    url(r'mis_solicitudes/$', ListarActividad.as_view(), name = 'mis_solicitudes'),
    url(r'^(?P<id>[\w.@+-]+)/editar/$', EditarActividad.as_view(), name = 'editar_actividad'),
    url(r'^(?P<id>[\w.@+-]+)/detalles/$', DetallesActividad.as_view(), name = 'detalles_actividad'),
    #url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='auth_logout'),
]

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', Inicio.as_view(), name = 'login' ),
    url(r'^usuarios/', include(urlpatterns_usuarios)),
    url(r'^solicitudes/', include(urlpatterns_solicitudes)),
]
