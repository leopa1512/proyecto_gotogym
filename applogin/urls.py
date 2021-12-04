from applogin import views  ##para poder llamar a las funciones creadas en Views.py
from django.urls import path
from django.contrib.auth import views as vistas_sesion  ##Vistas para el login
from applogin.views import *
from django.urls import re_path
from django.contrib.auth import views as auth_views
from django.conf.urls import url
from django.urls import reverse_lazy
from .views import MostrarUser, RegistroUser

app_name = "config"

urlpatterns = [
    path('l/', Home.as_view(), name='home'),
    path('', RedirectView.as_view(url='home', permanent=False), name='r_home'),  ##hace una redireccion hacia otra pagina
    path('login/', vistas_sesion.LoginView.as_view(template_name='apploginp/login.html'), name='login'),
    path('logout/', vistas_sesion.LogoutView.as_view(template_name='apploginp/home.html'), name='logout'),
    path('home/', vistas_sesion.LoginView.as_view(template_name='apploginp/home2.html'), name='home'),
    #path('home/gotogym', QuienesSomos.as_view(), name='home_quienessomos'),
    path('home/gotogym', vistas_sesion.LoginView.as_view(template_name='apploginp/home_quienesSomos.html'), name='home_quienessomos'),  ##De esta manera se puede iniciar sesion desde este template sin crear una Views
    path('home/preguntas_frecuentes', vistas_sesion.LoginView.as_view(template_name='apploginp/home_preguntasFrecuentes.html'), name='home_preguntasfrecuentes'),   ##De esta manera se puede iniciar sesion desde este template sin crear una Views
    path('home/devoluciones', vistas_sesion.LoginView.as_view(template_name='apploginp/home_devoluciones.html'), name='home_devoluciones'), ##De esta manera se puede iniciar sesion desde este template sin crear una Views
    path('home/cultura_corporativa', vistas_sesion.LoginView.as_view(template_name='apploginp/home_culturaCorporativa.html'), name='home_culturacorporativa'),  ##De esta manera se puede iniciar sesion desde este template sin crear una Views
    path('home/politicas_privacidad', vistas_sesion.LoginView.as_view(template_name='apploginp/home_politicayprivacidad.html'), name='home_politicayprivacidad'),   ##De esta manera se puede iniciar sesion desde este template sin crear una Views
    #path('home/contactanos', vistas_sesion.LoginView.as_view(template_name='apploginp/home_contactanos.html'), name='home_contactanos'),   ##De esta manera se puede iniciar sesion desde este template sin crear una Views
    #path('home/relaciones_inversionistas', vistas_sesion.LoginView.as_view(template_name='apploginp/home_relacionesConInversionistas.html'), name='home_relacionesconinversionistas'),   ##De esta manera se puede iniciar sesion desde este template sin crear una Views
    #path('home/trabaja_con_nosotros', vistas_sesion.LoginView.as_view(template_name='apploginp/home_trabajaConNosotros.html'), name='home_trabajaconnosotros'),   ##De esta manera se puede iniciar sesion desde este template sin crear una Views
    #path('home/sesion', HomeLogout.as_view(template_name='apploginp/home_logout.html'), name='home_sesion'),
    path('home/contactanos/', views.contactomail, name='home_contactanos'),
    path('home/trabaja_con_nosotros/', views.trabajaconnosotros, name='home_trabajaconnosotros'),
    path('home/relaciones_inversionistas/', views.relacioninversionistas, name='home_relacionesconinversionistas'),
    path('user/', MostrarUser.as_view(), name='list_user'),
    path('user/registro', RegistroUser.as_view(), name='registro_user'),
    
    url(
        r'^user/recovery/$', auth_views.PasswordResetView.as_view(
            template_name='apploginp/reset_pass_form.html',
            html_email_template_name='apploginp/reset_pass_email.html',),
            name='password_reset',
    ),

    url(
        r'^user/recovery/cambiar/$',
        auth_views.PasswordResetDoneView.as_view(
            template_name='apploginp/reset_pass_cambiar.html',
        ),
        name='password_reset_done',
    ),

    url(
        r'^user/recovery/(?P<uidb64>[0-9A-Za-z_\-]+)/'
        r'(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(
            success_url=reverse_lazy('home'),
            post_reset_login=True,
            template_name='apploginp/reset_pass_confirmar.html',
            post_reset_login_backend=(
                'django.contrib.auth.backends.AllowAllUsersModelBackend'
            ),
        ),
        name='password_reset_confirm',
    ),


]