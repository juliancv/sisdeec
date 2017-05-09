from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth.models import User, Group
from datetime import datetime
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.views.generic import CreateView, TemplateView
from django.template import RequestContext
from .models import *
from .forms import *

# Create your views here.

class Inicio(TemplateView):
    template_name = 'usuarios/index.html'

class PersonaCreateView(TemplateView):
    model = Persona
    template_name = 'usuarios/nuevo_usuario.html'

    def get_context_data(self, **kwargs):
        context = super(PersonaCreateView, self).get_context_data(**kwargs)
        persona_form = PersonaForm()

        context['persona_form'] = persona_form

        return context

    def post(self, request, *args, **kwargs):
        context = super(PersonaCreateView, self).get_context_data(**kwargs)
        form = PersonaForm(request.POST)

        if form.is_valid():
            nombres     = request.POST.get('nombres')
            apellidos   = request.POST.get('apellidos')
            identificacion = request.POST.get('identificacion')
            telefono    = request.POST.get('telefono')
            correo      = request.POST.get('correo')
            area_oficina = request.POST.get('area_oficina')
            password = request.POST.get('password')
            confirmar_pass = request.POST.get('confirmar_pass')

            nuevo_usuario = User.object.create_user(username = identificacion, password = password)
            nuevo_usuario.save()

            try:
                grupo = Group.objects.get(name = 'usuario_usuario')
                grupo.user_set.add(nuevo_usuario)
            except:
                grupo = Group()
                grupo.name = 'usuario_usuario'
                grupo.save()
                grupo.user_set.add(nuevo_usuario)

            nueva_persona = Persona(
                nombres = nombres,
                apellidos = apellidos,
                identificacion = identificacion,
                telefono = telefono,
                usuario = usuario_usuario,
                area_oficina = area_oficina,
                correo = correo
            )

            nueva_persona.save()

            self.request.session['registro_exitoso'] = 'registro'

            return HttpResponseRedirect('/usuarios/listado')
        else:
            context['persona_form'] = form
            return render(request, 'usuarios/nuevo_usuario.html')
