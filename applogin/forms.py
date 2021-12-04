from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.db import models
from django.forms import fields
from django import forms

from .models import Usuario

class UsuarioCreationForm(UserCreationForm):
    
    class Meta:
        model = Usuario
        fields = ("first_name","last_name","date_birth","num_telf","email",)
    
    def __init__(self,*args,**kwargs):
        super(UsuarioCreationForm,self).__init__(*args,**kwargs)


class UsuarioChangeForm(UserChangeForm):
    def __init__(self,*args,**kwargs):
        super(UsuarioChangeForm,self).__init__(*args,**kwargs)

    class Meta:
        model = Usuario
        fields = '__all__'


"""class UsuarioCreationForm(UserCreationForm):
    def __init__(self,*args,**kwargs):
        super(UsuarioCreationForm,self).__init__(*args,**kwargs)

    class Meta:
        model = Usuario
        fields = ("email",)


class UsuarioChangeForm(UserChangeForm):
    def __init__(self,*args,**kwargs):
        super(UsuarioChangeForm,self).__init__(*args,**kwargs)

    class Meta:
        model = Usuario
        fields = '__all__' """


"""class UsuarioForm(forms.ModelForm):
    class Meta: ##especificamos los datos a tomar
        model = Usuario
        fields = ['email','password']
        labels = {'email':"Correo electronico",
        'password':"Contraseña"}
        widget= {'email':forms.TextInput}   #indicamos el tipo de elemento HTML a utilizar

    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })"""