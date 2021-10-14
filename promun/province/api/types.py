from graphene_django import DjangoObjectType

from promun.province import models


class ProvinceType(DjangoObjectType):
    class Meta:
        model = models.Province
        only_fields = (
            'id',
            'name',
            'slug',
        )


class TownType(DjangoObjectType):
    class Meta:
        model = models.Town
        only_fields = (
            'id',
            'name',
            'slug',
        )


user_types = [
    ProvinceType, TownType
]