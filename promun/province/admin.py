from django.contrib import admin

from . import models


@admin.register(models.Province)
class ProvinceAdmin(admin.ModelAdmin):
    model = models.Province
    list_display = ['name', 'slug']
    fields = ('name',)


@admin.register(models.Town)
class TownAdmin(admin.ModelAdmin):
    model = models.Town
    list_display = ['name', 'slug']
    fields = ('name', 'province')
