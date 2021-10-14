import graphene
from graphql import GraphQLError

from promun.province.models import Province, Town


class CreateProvince(graphene.Mutation):
    status = graphene.Boolean()

    class Arguments:
        name = graphene.String()

    @staticmethod
    def mutate(root, info, name):
        Province.objects.create(name=name)
        return CreateProvince(status=True)


class CreateTown(graphene.Mutation):
    status = graphene.Boolean()

    class Arguments:
        name = graphene.String()
        province_slug = graphene.String()

    @staticmethod
    def mutate(root, info, name, province_slug):
        try:
            province = Province.objects.get(slug=province_slug)
            Town.objects.create(name=name, province=province)
            return CreateTown(status=True)
        except Province.DoesNotExist:
            return GraphQLError('Province slug doesn\'t exist')


class ProvinceMutation:
    add_province = CreateProvince.Field()
    add_town = CreateTown.Field()
