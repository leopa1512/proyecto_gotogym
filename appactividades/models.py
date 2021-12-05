from enum import unique
from django.db import models
from django.utils.translation import ugettext_lazy as _

#importamos la clase creada en la ruta applogin\models.py
from applogin.models import ClaseModelo

# Creamos el modelo Categoria_Act para "appactividades"
#la clase Categoria_Act esta heredando de la clase ClaseModelo y con ello heredara lo que se definio en applogin\models.py
class Categoria_Act(ClaseModelo):
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripción de las actividades',
        unique=True ##para indicar que la categoria creada NO se repita
    )

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper() ##Sobrescribimos para guardar la descripción en mayuscula
        super(Categoria_Act, self).save()

    class Meta:
        verbose_name_plural = "Categorias"


#creamo el modelo SubCategoria_Act para "appactividades"
class SubCategoria_Act(ClaseModelo):
    categ_activ = models.ForeignKey(Categoria_Act, on_delete=models.CASCADE)  ##Hacemos la relación con la PK del modelo Categoria_Act.
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripción de la subcategoria',
    )

    def __str__(self):
        return '{}:{}'.format(self.categ_activ.descripcion, self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper() ##Sobrescribimos para guardar todo en mayuscula.
        super(SubCategoria_Act, self).save()

    class Meta:
        verbose_name_plural = "SubCategorias"
        #usamos un Unique compuesto
        unique_together = ('categ_activ','descripcion')   #para que una SubCategoria NO se repita en una Categoria de la actividad.


#Creamos el modelo Actividades para "appactividades"
class Actividades(ClaseModelo):
    titulo = models.CharField(
        max_length=150,
        help_text='Titulo de la publicación',
        unique=True ##para indicar que la actividad creada NO se repita
    )
    descrip_act = models.CharField(_('descripcion publicación'),max_length=1000)
    date_inicio = models.DateField(_('fecha/hora inicio'), null=True)
    date_fin = models.DateField(_('fecha/hora fin'), null=True)
    recordar = models.BooleanField(_('recordatorio'), default=False)
    tiempo_recordar = models.IntegerField(_('tiempo recordatorio'),default=0)
    realizo_act = models.BooleanField(_('realizo actividad'), default=False)

    subcateg_act = models.ForeignKey(SubCategoria_Act, on_delete=models.CASCADE)  ##Hacemos la relación con la PK del modelo SubCategoria_Act.

    def __str__(self):
        return '{}'.format(self.titulo)

    def save(self):
        self.titulo = self.titulo.upper() ##Sobrescribimos para guardar todo en mayuscula
        super(Actividades, self).save()

    class Meta:
        verbose_name_plural = "Publicaciones"
        unique_together = ('subcateg_act','titulo')  #para que un titulo no se repita en una subcategoria.

