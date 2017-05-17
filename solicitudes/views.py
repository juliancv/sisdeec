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

class ActividadCreateView(TemplateView):

    model = Actividad
    template_name = 'solicitudes/nueva_solicitud.html'

    def get_context_data(self, **kwargs):
        context = super(ActividadCreateView, self).get_context_data(**kwargs)

        form = SolicitudForm()

        context['form_solicitud'] = form

        return context

    def post(self, request, *args, **kwargs):
        context = super(ActividadCreateView, self).get_context_data(**kwargs)

        form = SolicitudForm(request.POST)

        if form.is_valid():
            titulo = request.POST.get('titulo')
            resumen = request.POST.get('resumen')


            mi_solicitud = Actividad(

                titulo = titulo,
                resumen = resumen,
                solicitante_id = self.request.user

            )

            mi_solicitud.save()

            self.request.session['registro_exitoso'] = 'registro'
            return HttpResponseRedirect('/solicitudes/mis_solicitudes')
        else:
            context['form_solicitud'] = form
            return render(request, 'solicitudes/nueva_solicitud.html')

class ListarActividad(TemplateView):
    template_name = 'solicitudes/mis_solicitudes.html'

    def get_context_data(self, **kwargs):
        context = super(ListarActividad, self).get_context_data(**kwargs)

        actividades = Actividad.objects.all()

        context['actividades'] = actividades

        return context


class EditarActividad(TemplateView):
    template_name = 'solicitudes/editar.html'

    def get_context_data(self, **kwargs):
        context = super(EditarActividad, self).get_context_data(**kwargs)
        context['actividad'] = Actividad.objects.get(act_id = kwargs['id'])
        context['actividad_form_editar'] = SolicitudEditForm()

        usuarios = User.objects.all().filter(groups = 1)

        responsables = Persona.objects.filter(usuario__in = usuarios)

        context['responsables'] = responsables

        return context

    def post(self, request, *args, **kwargs):
        context = super(EditarActividad, self).get_context_data(**kwargs)
        actividad = Actividad.objects.get(act_id = kwargs['id'])
        context['actividad'] = actividad
        #responsable = User.objects.filter(Persona.nombres = request.POST['responsable'])
        actividad.prioridad = request.POST['prioridad']
        actividad.comentarios = request.POST['comentarios']

        actividad.save()

        return HttpResponseRedirect('/solicitudes/'+kwargs['id']+'/detalles')

class DetallesActividad(TemplateView):
    template_name = 'solicitudes/detalles.html'

    def get_context_data(self, **kwargs):
        context = super(DetallesActividad, self).get_context_data(**kwargs)
        context['actividad'] = Actividad.objects.get(act_id = kwargs['id'])
        context['id']        = kwargs['id']

        return context
