from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _

from .models import Usuario
from .forms import UserChangeForm,UserCreationForm, UsuarioChangeForm, UsuarioCreationForm

class UsuarioAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('dni_tipo','dni', 'first_name', 'last_name', 'date_birth', 'num_telf', 'num_cell','pais','ciudad','direccion','cod_postal','imagen')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name','last_name','date_birth','num_telf','email', 'password1', 'password2')}
        ),
    )
    form = UsuarioChangeForm
    add_form = UsuarioCreationForm
    list_display = ('dni','email','first_name','last_name','pais','is_active','is_staff')
    search_fields = ('email','first_name','last_name','dni')
    ordering = ('email',)


admin.site.register(Usuario,UsuarioAdmin)
