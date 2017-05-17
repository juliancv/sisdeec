from django import forms
from .models import *
from usuarios.models import *

class SolicitudForm(forms.Form):

    titulo = forms.CharField(required = True)
    resumen = forms.CharField(widget = forms.Textarea, required = True)

    titulo.widget.attrs.update({
                                'id':'id_titulo',
                                'class':'form-control',
                                'name':'Titulo',
                                'Placeholder':'Ingrese el asunto',
                                'type' :  'text'
    })

    resumen.widget.attrs.update({
                                'id' : 'id_resumen',
                                'class' : 'form-control',
                                'name'  : 'Resumen',
                                'Placeholder' : 'Ingrese la descripcion de la labor requerida ',
                                'type' : 'text'
    })

class SolicitudEditForm(forms.Form):

    OPT_PRIORIDAD = (('1','1'),('2','2'),('3','3'),('4','4'),('5','5'))
    OPT_ESTADO = (('Nuevo', 'Nuevo'),('Rechazado', 'Rechazado'))

    titulo       = forms.CharField(required = True)
    resumen      = forms.CharField(widget = forms.Textarea, required = True)
    responsable  = forms.ChoiceField( required = True, widget = forms.Select)
    prioridad    = forms.ChoiceField( required = True, widget = forms.Select, choices = OPT_PRIORIDAD)
    estado       = forms.ChoiceField( required = True, widget = forms.Select, choices = OPT_ESTADO)
    comentarios  = forms.CharField(widget = forms.Textarea, required = True)

    titulo.widget.attrs.update({
                                'id':'id_titulo',
                                'class':'form-control',
                                'name':'Titulo',
                                'Placeholder':'Ingrese el asunto',
                                'type' :  'text'
    })

    resumen.widget.attrs.update({
                                'id' : 'id_resumen',
                                'class' : 'form-control',
                                'name'  : 'Resumen',
                                'Placeholder' : 'Ingrese la descripcion de la labor requerida ',
                                'type' : 'text'
    })

    prioridad.widget.attrs.update({
                                'id' : 'id_prioridad',
                                'class' : 'form-control',
                                'name'  : 'prioridad',
    })

    estado.widget.attrs.update({
                                'id' : 'id_estado',
                                'class' : 'form-control',
                                'name'  : 'estado',
    })

    comentarios.widget.attrs.update({
                                'id' : 'id_comentarios',
                                'class' : 'form-control',
                                'name'  : 'comentarios',
                                'value' : 'holamundo',
                                'type' : 'text'
    })
