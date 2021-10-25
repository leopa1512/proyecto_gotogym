from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.db import models
from django.forms import fields

from .models import Usuario

class UsuarioCreationForm(UserCreationForm):
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
        fields = '__all__'
