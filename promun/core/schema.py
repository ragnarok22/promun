import graphene
from graphene import ObjectType

from promun.province.api.schema import province_types, ProvinceQuery, ProvinceMutation

types = province_types


class Query(ProvinceQuery, ObjectType):
    pass


class Mutation(ObjectType):
    pass


schema = graphene.Schema(
    types=types,
    query=Query,
    # mutation=Mutation
)
