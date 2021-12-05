from enum import unique
from django.db import models
from django.utils.translation import ugettext_lazy as _

#importamos la clase creada en la ruta applogin\models.py
from applogin.models import ClaseModelo

# Creamos el modelo Categoria_R para "apprevista"
#la clase Categoria_R esta heredando de la clase ClaseModelo y con ello heredara lo que se definio en applogin\models.py
class Categoria_R(ClaseModelo):
    descripcion = models.CharField(
        max_length=200,
        help_text='Descripción de la categoria de revista',
        unique=True ##para indicar que la categoria creada NO se repita
    )

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper() ##Sobrescribimos para guardar la descripción en mayuscula
        super(Categoria_R, self).save()

    class Meta:
        verbose_name_plural = "Categorias"


#creamo el modelo SubCategoria_R para "apprevista"
class SubCategoria_R(ClaseModelo):
    categ_revist = models.ForeignKey(Categoria_R, on_delete=models.CASCADE)  ##Hacemos la relación con la PK del modelo categoria.
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripción de la subcategoria',
    )

    def __str__(self):
        return '{}:{}'.format(self.categ_revist.descripcion, self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper() ##Sobrescribimos para guardar todo en mayuscula
        super(SubCategoria_R, self).save()

    class Meta:
        verbose_name_plural = "SubCategorias"
        #usamos un Unique compuesto
        unique_together = ('categ_revist','descripcion')   #para que una SubCategoria NO se repita en una Categoria de la revista


#Creamos el modelo Publicacion para "apprevista"
class Publicacion(ClaseModelo):
    titulo = models.CharField(
        max_length=150,
        help_text='Titulo de la publicación',
        unique=True ##para indicar que el titulo creado NO se repita
    )
    descrip_publ = models.CharField(_('descripcion publicación'),max_length=1000)
    imag_prod = models.ImageField(_('imagen publicación'), upload_to='imagen_user', null=True)

    subcateg_r = models.ForeignKey(SubCategoria_R, on_delete=models.CASCADE)  ##Hacemos la relación con la PK del modelo Marca.

    def __str__(self):
        return '{}'.format(self.titulo)

    def save(self):
        self.titulo = self.titulo.upper() ##Sobrescribimos para guardar todo en mayuscula.
        super(Publicacion, self).save()

    class Meta:
        verbose_name_plural = "Publicaciones"
        unique_together = ('subcateg_r','titulo')  #para que un titulo NO se repita en una subcategoria.