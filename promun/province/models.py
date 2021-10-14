from django.db import models

from .utils import slugify


class SlugifyModel(models.Model):
    name = models.CharField(verbose_name='Nombre', max_length=50)
    slug = models.CharField(verbose_name='Slug', max_length=50)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True
        ordering = ['name']


class Province(SlugifyModel):
    class Meta:
        verbose_name = 'Provincia'
        verbose_name_plural = 'Provincias'


class Town(SlugifyModel):
    province = models.ForeignKey(to='Province', on_delete=models.CASCADE, related_name='provincias')

    class Meta:
        verbose_name = 'Municipio'
        verbose_name_plural = 'Municipios'
