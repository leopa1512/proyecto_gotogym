from enum import unique
from django.db import models
from django.utils.translation import ugettext_lazy as _

#importamos la clase creada en la ruta applogin\models.py
from applogin.models import ClaseModelo

# Creamos el modelo Categoria_Act para "apppregbienestar"
#la clase Categoria_Act esta heredando de la clase ClaseModelo y con ello heredara lo que se definio en applogin\models.py
class Categoria_PB(ClaseModelo):
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripción de la categoria',
        unique=True ##para indicar que la categoria creada NO se repita
    )

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper() ##Sobrescribimos para guardar la descripción en mayuscula
        super(Categoria_PB, self).save()

    class Meta:
        verbose_name_plural = "Categorias"


#creamo el modelo SubCategoria_PB para "apppregbienestar"
class SubCategoria_PB(ClaseModelo):
    categ_pb = models.ForeignKey(Categoria_PB, on_delete=models.CASCADE)  ##Hacemos la relación con la PK del modelo categoria.
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripción de la subcategoria',
    )

    def __str__(self):
        return '{}:{}'.format(self.categ_pb.descripcion, self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper() ##Sobrescribimos para guardar todo en mayuscula.
        super(SubCategoria_PB, self).save()

    class Meta:
        verbose_name_plural = "SubCategorias"
        #usamos un Unique compuesto
        unique_together = ('categ_pb','descripcion')   #para que una SubCategoria NO se repita en una Categoria de las preguntas de bienestar.


#Creamos el modelo Actividades para "apppregbienestar"
class Preg_Bienestar(ClaseModelo):
    titulo = models.CharField(
        max_length=150,
        help_text='Titulo de la pregunta de bienestar.',
        unique=True ##para indicar que el titulo de la pregunta creada NO se repita.
    )
    descrip_pb = models.CharField(_('descripcion publicación'),max_length=1000)
    date_inicio = models.DateField(_('fecha/hora inicio'), null=True)
    date_fin = models.DateField(_('fecha/hora fin'), null=True)
    recordar = models.BooleanField(_('recordatorio'), default=False)
    tiempo_recordar = models.IntegerField(_('tiempo recordatorio'),default=0)
    respuesta_pb = models.CharField(_('recordatorio'), max_length=2, blank=True)

    subcateg_pb = models.ForeignKey(SubCategoria_PB, on_delete=models.CASCADE)  ##Hacemos la relación con la PK del modelo SubCategoria_PB.

    def __str__(self):
        return '{}'.format(self.titulo)

    def save(self):
        self.titulo = self.titulo.upper() ##Sobrescribimos para guardar todo en mayuscula.
        super(Preg_Bienestar, self).save()

    class Meta:
        verbose_name_plural = "Publicaciones"
        unique_together = ('subcateg_pb','titulo')  #para que un titulo no se repita en una subcategoria.


