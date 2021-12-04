from enum import unique
from django.db import models

#importamos la clase creada en la ruta applogin\models.py
from applogin.models import ClaseModelo

# Creamos el modelo para "inv"
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
        help_text='Descripción de la categoria',
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
        unique=True ##para indicar que la categoria creada NO se repita
    )

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper() ##Sobrescribimos para guardar todo en mayuscula
        super(Marca, self).save()

    class Meta:
        verbose_name_plural = "Marcas"