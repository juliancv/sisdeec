from django import forms
from .models import *



class PersonaForm(forms.Form):

    OFICINAS = ((1, u'Programa Egresados'), (2, u'Programa Emprendedores'), (3, u'Practicas & pasantias'), (4, u'Educacion continua'),(5, u'Proyectos'),(6, u'Pilos'), (7, u'DEEC'),)
    OPT_USR = ((1, u'General'),(2, u'Monitor'))

    nombres         = forms.CharField( required = True )
    apellidos       = forms.CharField( required = True )
    identificacion  = forms.IntegerField( required = True )
    telefono        = forms.IntegerField( required = True )
    correo          = forms.EmailField( required = True )
    area_oficina    = forms.ChoiceField( required = True, widget = forms.Select, choices = OFICINAS )
    tipo_usuario    = forms.ChoiceField( required = True, widget = forms.Select, choices = OPT_USR)

    nombres.widget.attrs.update({ 'id' : 'id_nombres',
                                'class': 'form-control',
                                'name' : 'Nombres',
                                'placeholder' : 'Ingrese su nombre completo',
                                'type' : 'text'})

    apellidos.widget.attrs.update({ 'id' : 'id_apellidos',
                                'class': 'form-control',
                                'name' : 'Apellidos',
                                'placeholder' : 'Ingrese sus apellidos',
                                'type' : 'text'})

    identificacion.widget.attrs.update({ 'id' : 'id_identificacion',
                                'class': 'form-control',
                                'name' : 'Identificacion',
                                'placeholder' : 'Ingrese su numero de identificacion',
                                'type' : 'text'})

    telefono.widget.attrs.update({ 'id' : 'id_telefono',
                                'class': 'form-control',
                                'name' : 'Telefono',
                                'placeholder' : 'Ingrese su numero de contacto',
                                'type' : 'text'})

    correo.widget.attrs.update({ 'id' : 'id_correo',
                                'class': 'form-control',
                                'name' : 'Correo',
                                'placeholder' : 'Ingrese su correo electronico',
                                'type' : 'text'})

    tipo_usuario.widget.attrs.update({ 'id' : 'id_tipo_usuario',
                                'class': 'form-control',
                                'name' : 'tipo_usuario',
                                })

    area_oficina.widget.attrs.update({ 'id' : 'id_area_oficina',
                                'class': 'form-control',
                                'name' : 'area_oficina',
                            })
