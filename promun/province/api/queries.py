import graphene
from .types import TownType, ProvinceType
from ..models import Province


class ProvinceQuery:
    all_provinces = graphene.List(ProvinceType)

    @staticmethod
    def resolve_all_provinces(*args, **kwargs):
        return Province.objects.all()
