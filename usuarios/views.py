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
#from .forms import *

# Create your views here.

class Inicio(TemplateView):
    template_name = 'usuarios/index.html'
