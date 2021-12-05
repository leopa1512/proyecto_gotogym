from enum import unique
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

#importamos la clase creada en la ruta applogin\models.py
from applogin.models import ClaseModelo
from appcatalogo.models import Producto     #importamos la clase creada en la ruta appcatalogo\models.py
# Create your models here.

# Creamos el modelo para "appcompra"
#la clase DescuentoF esta heredando de la clase ClaseModelo y con ello heredara lo que se definio en applogin\models.py
class DescuentoF(ClaseModelo):
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripción del descuento',
        unique=True ##para indicar que el descuento creado NO se repita
    )
    cant_desc = models.IntegerField(_('cantidad del descuento'),default=0)

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper() ##Sobrescribimos para guardar todo en mayuscula
        super(DescuentoF, self).save()

    class Meta:
        verbose_name_plural = "Descuentos"


# Creamos el modelo Factura para "appcompra"
class Factura(ClaseModelo):
    cod_factura = models.CharField(
        max_length=50,
        help_text='codigo factura'
    )
    tipo_factura = models.CharField(_('tipo facturacion'),max_length=20)
    dni = models.IntegerField(_('numero identificacion'), null=True, blank=True)
    direccion = models.CharField(_('direccion'), max_length=60, blank=True)
    email = models.EmailField(_('direccion email'), max_length=254, null=True, blank=True)
    num_telf = models.CharField(_('numero telefono'), max_length=20, blank=True)
    num_cell = models.CharField(_('numero celular'), max_length=20, blank=True)
    descripcion = models.CharField(_('descripción producto'),max_length=200)
    est_pago = models.CharField(_('estado pago'),max_length=15,blank=True)
    Sub_total = models.IntegerField(_('sun total'),default=0)
    impuesto = models.IntegerField(_('impuesto'),default=0)
    total_pagar = models.IntegerField(_('total pagar'),default=0)
    plan_contrato = models.IntegerField(_('plan contratado'), null=True, blank=True)

    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)  ##Hacemos la relación con la PK del modelo Producto de "appcatalogo".
    descuentof = models.ForeignKey(DescuentoF, on_delete=models.CASCADE)  ##Hacemos la relación con la PK del modelo Descuento.

    def __str__(self):
        return '{}'.format(self.cod_factura)

    class Meta:
        verbose_name_plural = "Facturas"


# Creamos el modelo EstadoPedido para "appcompra"
class EstadoPedido(ClaseModelo):
    descrip_pedido = models.CharField(max_length=1000,help_text='Descripción del pedido',blank=True)
    descrip_estado = models.CharField(max_length=500,help_text='Descripción del estado',blank=True)
    cod_factura = models.CharField(_('codigo factura'),max_length=50)

    factura = models.ForeignKey(Factura, on_delete=models.CASCADE)  ##Hacemos la relación con la PK del modelo Factura.

    def __str__(self):
        return '{}'.format(self.descrip_estado)

    class Meta:
        verbose_name_plural = "EstadoPedidos"


# Creamos el modelo ProductoInteres para "appcompra"
class ProductoInteres(ClaseModelo):
    date_observa = models.DateTimeField(_('date observa'),help_text='Fecha/hora que observo un producto',default=timezone.now)
    est_pago = models.CharField(_('estado pago'),max_length=15)
    descrip_prod = models.CharField(_('descripcion producto'),max_length=200)

    factura = models.ForeignKey(Factura, on_delete=models.CASCADE)  ##Hacemos la relación con la PK del modelo Factura.
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)  ##Hacemos la relación con la PK del modelo Producto.

    def __str__(self):
        return '{}'.format(self.est_pago)

    class Meta:
        verbose_name_plural = "ProductosInteres"