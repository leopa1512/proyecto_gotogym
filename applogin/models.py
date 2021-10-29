from django.db import models
from django.utils import timezone
from django.utils.http import urlquote
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import UsuarioManager

##Al heredar de AbstractBaseUser define automaticamente un campo contraseña
##PermissionsMixin permite generar los permisos de usuarios.
class Usuario(AbstractBaseUser,PermissionsMixin):
    dni = models.IntegerField(_('cedula'), null=True, blank=True)
    email = models.EmailField(_('direccion email'), max_length=254, unique=True)
    first_name = models.CharField(_('nombres'), max_length=30, blank=True)
    last_name = models.CharField(_('apellidos'), max_length=30, blank=True)
    date_birth = models.DateField(_('fecha nacimiento'), null=True)
    num_telf = models.CharField(_('numero telefono'), max_length=20, blank=True)
    num_cell = models.CharField(_('numero celular'), max_length=20, blank=True)
    is_staff = models.BooleanField(_('es staff'), default=False,
        help_text=_('Indica si el usuario puede iniciar sesión en admin '))
    is_active = models.BooleanField(_('activo'), default=True,
        help_text=_('Designa si este usuario debe ser tratado como activo'
                    'Deseleccione esto en lugar de eliminar cuentas.'))
    date_joined = models.DateTimeField(_('fecha registro'), default=timezone.now)
    imagen = models.ImageField(_('imagen usuario'), upload_to='imagen_user', null=True)


    USERNAME_FIELD = 'email' ##Le decimos que el usuario sera el correo electronico
    REQUIRED_FIELDS = []    #especifica los demas campos requeridos.

    objects = UsuarioManager()  #Le indicamos que utilice la configuracion del fichero managers.py

    class Meta:
        verbose_name = _('usuario') #para traducir el nombre de los campos creados
        verbose_name_plural = _('usuarios')

    def get_absolute_url(self):
        return "/users/%s" % urlquote(self.email)   #se sobrescribe para que el usuario sea el correo
    
    def get_full_name(self):
        full_name = "%s %s" % (self.first_name,self.last_name) ##retorna el nombre y apellido
        return full_name.strip()
    
    def get_short_name(self):
        return self.first_name
