from enum import unique
from django.db import models
from django.utils.translation import ugettext_lazy as _

#importamos la clase creada en la ruta applogin\models.py
from applogin.models import ClaseModelo

# Creamos el modelo para "appcatalogo"
#la clase Categoria esta heredando de la clase ClaseModelo y con ello heredara lo que se definio en applogin\models.py
class Categoria(ClaseModelo):
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripción de la categoria',
        unique=True ##para indicar que la categoria creada NO se repita
    )

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper() ##Sobrescribimos para guardar la descripción en mayuscula
        super(Categoria, self).save()

    class Meta:
        verbose_name_plural = "Categorias"


#creamo el modelo para SubCategoria para "appcatalogo"
class SubCategoria(ClaseModelo):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)  ##Hacemos la relación con la PK del modelo categoria.
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripción de la subcategoria',
    )

    def __str__(self):
        return '{}:{}'.format(self.categoria.descripcion, self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper() ##Sobrescribimos para guardar todo en mayuscula
        super(SubCategoria, self).save()

    class Meta:
        verbose_name_plural = "Sub Categoria"
        #usamos un Unique compuesto
        unique_together = ('categoria','descripcion')   #para que una SubCategoria NO se repita en una Categoria


# Creamos el modelo Marca para "appcatalogo"
class Marca(ClaseModelo):
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripción de la Marca',
        unique=True ##para indicar que la marca creada NO se repita
    )

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper() ##Sobrescribimos para guardar todo en mayuscula
        super(Marca, self).save()

    class Meta:
        verbose_name_plural = "Marcas"


# Creamos el modelo Marca para "appcatalogo"
class Descuento(ClaseModelo):
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
        super(Descuento, self).save()

    class Meta:
        verbose_name_plural = "Descuentos"


# Creamos el modelo Producto para "appcatalogo"
class Producto(ClaseModelo):
    num_serie = models.CharField(
        max_length=20,
        unique=True ##para indicar que el producto creado NO se repita
    )
    descripcion = models.CharField(max_length=200)
    codigo_barra = models.CharField(_('código de barra'),max_length=50)
    precio = models.FloatField(_('precio del producto'),default=0)
    cant_existencia = models.IntegerField(_('cantidad en existencia'),default=0)
    ultima_compra = models.DateField(_('ultima compra'),null=True, blank=True)
    imag_prod = models.ImageField(_('imagen producto'), upload_to='imagen_user', null=True)

    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)  ##Hacemos la relación con la PK del modelo Marca.
    descuento = models.ForeignKey(Descuento, on_delete=models.CASCADE)  ##Hacemos la relación con la PK del modelo Descuento.
    subcategoria = models.ForeignKey(SubCategoria, on_delete=models.CASCADE)    ##Hacemos la relación con la PK del modelo SubCategoria.

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper() ##Sobrescribimos para guardar todo en mayuscula
        super(Producto, self).save()

    class Meta:
        verbose_name_plural = "Productos"
        unique_together = ('num_serie','codigo_barra')  #para que un numero de serie NO se repita en un codigo de barra