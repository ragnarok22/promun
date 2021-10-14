import graphene
from django.contrib.auth.decorators import login_required

from promun.province.models import Province


class CreateProvince(graphene.Mutation):
    status = graphene.Boolean()

    class Arguments:
        name = graphene.String()

    @staticmethod
    def mutate(root, info, name):
        Province.objects.create(name=name)
        return CreateProvince(status=True)


class ProvinceMutation:
    add_province = CreateProvince.Field()
