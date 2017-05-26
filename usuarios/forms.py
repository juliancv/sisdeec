from django import forms
from .models import *

class LoginForm(forms.Form):

    usuario     = forms.CharField(required = True)
    password    = forms.CharField(required = True, widget = forms.PasswordInput)

    usuario.widget.attrs.update({ 'id' : 'id_usuario',
                                'class': 'form-control',
                                'name' : 'Nombres',
                                'placeholder' : 'Ingrese su usuario',
                                'type' : 'text'})

    password.widget.attrs.update({ 'id' : 'id_password',
                                'class': 'form-control',
                                'name' : 'Password',
                                'placeholder' : 'Ingrese su contraseña',
                                'type' : 'text'})

class PersonaForm(forms.Form):

    OFICINAS = (('Programa Egresados', u'Programa Egresados'),
                ('Programa Emprendedores', u'Programa Emprendedores'),
                 ('Practicas & pasantias', u'Practicas & pasantias'),
                 ('Educacion continua', u'Educacion continua'),
                 ('Proyectos', u'Proyectos'),
                 ('Pilos', u'Pilos'),
                  ('DEEC', u'DEEC'),)
    OPT_USR = (('General', u'General'),('Monitor', u'Monitor'))

    nombres         = forms.CharField( required = True)
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
