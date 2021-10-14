import graphene
from .types import TownType, ProvinceType
from ..models import Province, Town


class ProvinceQuery:
    all_provinces = graphene.List(ProvinceType)
    towns_by_province = graphene.List(TownType, province=graphene.String())

    def resolve_all_provinces(self, info):
        return Province.objects.all()

    def resolve_towns_by_province(self, info, province):
        return Town.objects.filter(province__slug=province)
