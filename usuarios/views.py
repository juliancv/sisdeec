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

class Home(TemplateView):
    template_name = 'usuarios/index.html'

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)

        usuario = self.request.user

        context['usuario'] = usuario

        return context

class Inicio(TemplateView):
    template_name = 'login.html'


    def get_context_data(self, **kwargs):
        context = super(Inicio, self).get_context_data(**kwargs)

        form = LoginForm()

        context['login_form'] = form

        return context

    def post(self, request, *args, **kwargs):
        context = super(Inicio, self).get_context_data(**kwargs)

        form = LoginForm(request.POST)

        if form.is_valid():
            username = request.POST.get('usuario')
            password = request.POST.get('password')

            user = authenticate(username = username, password = password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect('usuarios/index.html', context)
        else:
            context['nuevo_usuario'] = 'usuario o contrase;a invalidos'
            return render(request, 'usuarios/index.html', context)


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
            tipo_usuario = request.POST.get('tipo_usuario')

            password = nombres[0:1] + identificacion + apellidos[0:1]

            nuevo_usuario = User.objects.create_user(username = identificacion, password = password)
            nuevo_usuario.save()

            if tipo_usuario == "General":
                try:
                    grupo = Group.objects.get(name = 'usuario_usuario')
                    grupo.user_set.add(nuevo_usuario)
                except:
                    grupo = Group()
                    grupo.name = 'usuario_usuario'
                    grupo.save()
                    grupo.user_set.add(nuevo_usuario)
            else:
                try:
                    grupo = Group.objects.get(name = 'usuario_monitor')
                    grupo.user_set.add(nuevo_usuario)
                except:
                    grupo = Group()
                    grupo.name = 'usuario_monitor'
                    grupo.save()
                    grupo.user_set.add(nuevo_usuario)


            nueva_persona = Persona(
                nombres = nombres,
                apellidos = apellidos,
                identificacion = identificacion,
                telefono = telefono,
                usuario = nuevo_usuario,
                area_oficina = area_oficina,
                correo = correo
            )

            nueva_persona.save()

            self.request.session['registro_exitoso'] = 'registro'

            return HttpResponseRedirect('/usuarios/lista_usuarios.html')
        else:
            context['persona_form'] = form
            return render(request, 'usuarios/nuevo_usuario.html')


class LoginView(TemplateView):
    template_name = "login.html"

    print("$$$$$$$$$$$$")

    def get_context_data(self, **kwargs):
        context = super(LoginView, self).get_context_data(**kwargs)

        print("$$$$$$$$$$$$")
        print(context)

    def post(self, request, *args, **kwargs):
        context = super(LoginView, self).get_context_data(**kwargs)

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username, password = password)

        print ("########################")
        print (user.username)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect('usuarios/index.html', context)
        else:
            context['nuevo_usuario'] = 'usuario o contrase;a invalidos'
            return render(request, 'usuarios/index.html', context)

class ListarUsuarios(TemplateView):
    template_name = "usuarios/lista_usuarios.html"

    def get_context_data(self, **kwargs):
        context = super(ListarUsuarios, self).get_context_data(**kwargs)

        usuarios = Persona.objects.all()

        context['usuarios'] = usuarios

        return context
