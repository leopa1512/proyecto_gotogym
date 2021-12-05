from enum import unique
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

#importamos la clase creada en la ruta applogin\models.py
from applogin.models import ClaseModelo
from appcompra.models import Factura    #importamos la clase creada en la ruta appcompras\models.py


#Creamos el modelo para "appplan"
#la clase TipoPlan esta heredando de la clase ClaseModelo y con ello heredara lo que se definio en applogin\models.py
class TipoPlan(ClaseModelo):
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripción del tipo de plan',
        unique=True ##para indicar que el tipo de plan creada NO se repita
    )
    tipo_plan = models.CharField(_('tipo plan'),max_length=20)
    cant_user = models.IntegerField(_('cantidad de usuarios'),default=0)
    preciop = models.FloatField(_('precio del plan'),default=0)

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper() ##Sobrescribimos para guardar la descripción en mayuscula
        super(TipoPlan, self).save()

    class Meta:
        verbose_name_plural = "TipoPlanes"


#Creamos el modelo para "appplan"
class Contratado(ClaseModelo):
    descripcion = models.CharField(_('tipo plan'),max_length=20)
    est_pago = models.CharField(_('estado pago'),max_length=15)
    date_vence = models.DateField(_('fecha vence plan'), null=True)

    tipoplan = models.ForeignKey(TipoPlan, on_delete=models.CASCADE)  ##Hacemos la relación con la PK del modelo TipoPlan.
    descuento = models.ForeignKey(Factura, on_delete=models.CASCADE)  ##Hacemos la relación con la PK del modelo Descuento.

    def __str__(self):
        return '{}:{}'.format(self.user_crea.first_name, self.tipoplan.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper() ##Sobrescribimos para guardar todo en mayuscula
        super(Contratado, self).save()

    class Meta:
        verbose_name_plural = "Contratados"
        unique_together = ('tipoplan','user_crea')  #para que un usuario NO contrate varios planes al mismo tiempo