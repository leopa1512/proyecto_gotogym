from django.shortcuts import render
from django.views.generic import *
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy

from django.core.mail import EmailMessage, send_mail, EmailMultiAlternatives
from django.conf import settings

import smtplib, ssl
import email
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import os

from django.views import generic
from .models import Usuario
from .forms import UsuarioCreationForm #, UsuarioForm

##Utilisando los Mixin se puede indicar que si un usuario no ha iniciado sesion
##Lo redirija por ejemplo a la  ventana de logeo o a la que indiquemos.
#class Home(LoginRequiredMixin, TemplateView):
    #template_name = 'apploginp/home.html'
    #login_url = 'config:login'

class Home(generic.TemplateView):
    template_name = 'apploginp/home.html'


#Para enviar un correo en "Contatenos"
def contactomail(request):
        if request.method == 'POST':
            asunto = 'Contacto GoToGym'
            if request.POST["agendar"] == '1':
                agendar_r = "Solicita agendar una reunión."
                message=request.POST["mensaje"] + ".\n\n" + "Correo del remitente: " + request.POST["email"] + "\n" + agendar_r
            else:
                message=request.POST["mensaje"] + ".\n\n" + "Correo del remitente: " + request.POST["email"]
            
            email_from = settings.EMAIL_HOST_USER   #correo de donde saldran los mensajes
            recipient_list = ["leopa_1512@hotmail.com"] #correo donde llegaran los mensajes

            if (len(message) > 0):
                send_mail(asunto, message, email_from, recipient_list)
                message = ""

        return render(request, "apploginp/home_contactanos.html")



#Para enviar correo en "Trabaja con Nosotros"
##Y enviar un documento adjunto al correo
def trabajaconnosotros(request):
    if request.method == 'POST':
        servidor = 'smtp.gmail.com'
        puerto = 465
        remitente = 'leo.parrales1512@gmail.com'  #correo de donde saldran los mensajes
        clave = 'xgnlhliiipghwelf'
        receptor = 'leopa_1512@hotmail.com'
        contexto = ssl.create_default_context()
        asunto = 'Trabaja con Nosotros'
        correo_r = "Correo del Contacto: " + request.POST["email"]
        nombre = "Nombre: " + request.POST["nombre"]
        apellido = "Apellido: " + request.POST["apellido"]
        dni = "Identificación: " + request.POST["dni"]
        pais = "País: " + request.POST["pais"]
        ciudad = "Ciudad: " + request.POST["ciudad"]
        direccion = "Dirección: " + request.POST["direccion"]
        telefono = "Num. Telefono: " + request.POST["telefono"]
        cuerpo = correo_r +".\n"+ nombre +".\n"+ apellido +".\n"+ dni +".\n"+ pais +".\n"+ ciudad +".\n"+ direccion +".\n"+ telefono

        message = MIMEMultipart()
        message['Subject'] = asunto
        message['From'] = remitente
        message['To'] = receptor

        message.attach(MIMEText(cuerpo, 'plain'))
        archivo = request.POST["curriculum"]
        #archivo = 'C:\\Users\\Pc\\Downloads\\grupo.pdf'

        #abrimos el documento en modo binario
        with open('C:\\Users\\Pc\\Downloads\\' + archivo, 'rb') as adjunto:
            pdf = MIMEBase('application','octet-stream')
            pdf.set_payload(adjunto.read())

        #lo codificamos en ascii para poder enviarlo
        encoders.encode_base64(pdf)
        pdf.add_header('Content-Disposition', f'attachment; filename={archivo}',)

        message.attach(pdf)
        texto = message.as_string()

        with smtplib.SMTP_SSL(servidor,puerto, context=contexto) as s:
            s.login(remitente, clave)
            s.sendmail(remitente, receptor, texto)

    return render(request, "apploginp/home_trabajaConNosotros.html")


##Para enviar formulario por correo
def relacioninversionistas(request):
        if request.method == 'POST':
            asunto = 'Relaciones con Inversionistas'
            correo_r = "Correo del Contacto: " + request.POST["email"]
            nombre = "Nombre: " + request.POST["nombre"]
            apellido = "Apellido: " + request.POST["apellido"]
            trabajo = "Tipo de trabajo: " + request.POST["trabajo"]
            compania = "Compañia: " + request.POST["compania"]
            linkedin = "Linkedin: " + request.POST["linkedin"]
            mensaje = "Mensaje: \n" + request.POST["mensaje"]

            message= correo_r +".\n"+ nombre +".\n"+ apellido +".\n"+ trabajo +".\n"+ compania +".\n"+ linkedin +".\n\n"+ mensaje
            email_from = settings.EMAIL_HOST_USER   #correo de donde saldran los mensajes
            recipient_list = ["leopa_1512@hotmail.com"] #correo donde llegaran los mensajes

            if (len(message) > 0):
                send_mail(asunto, message, email_from, recipient_list)
                message = ""

        return render(request, "apploginp/home_relacionesConInversionistas.html")


##Mostrar Listado de usuarios registrados
class MostrarUser(LoginRequiredMixin, generic.ListView):
    model = Usuario
    template_name = 'apploginp/list_user.html'
    context_object_name = 'obj' #cambio el nombre al objeto
    login_url = 'applogin:login'   #Si no esta logeado lo redirige 


#define la ruta del formulario de registro del usuario
#luego de registrado se redirige a otra pagina
class RegistroUser(generic.CreateView):
    model = Usuario
    template_name = 'apploginp/registro_user.html'
    context_object_name = 'obj' #cambio el nombre al objeto
    form_class = UsuarioCreationForm
    success_url = reverse_lazy('applogin:list_user')   #hace una redireccion

    def form_valid(self, form):
        form.instance.user_crea = self.request.user #para optener el usuario que crea
        return super().form_valid(form)


"""class RegistroUser(LoginRequiredMixin, generic.CreateView):
    model = Usuario
    template_name = 'apploginp/registro_user.html'
    context_object_name = 'obj' #cambio el nombre al objeto
    form_class = UsuarioForm
    success_url = reverse_lazy('applogin:list_user')   #hace una redireccion
    login_url = 'applogin:login'   #Si no esta logeado lo redirige 

    def form_valid(self, form):
        form.instance.user_crea = self.request.user #para optener el usuario que crea
        return super().form_valid(form)"""
