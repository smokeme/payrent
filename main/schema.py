import graphene
from graphene import relay

from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import *


class Paci(DjangoObjectType):
    complex = graphene.String()

    class Meta:
        model = Renter

    def get_complex(self, info):
        return self.complex.name


class Query(graphene.ObjectType):
    paci = graphene.Field(Paci, id=graphene.Int())

    def resolve_paci(self, info, **kwargs):
        id = kwargs.get("id")
        if id is not None:
            return Renter.objects.get(pk=id)
        return None


schema = graphene.Schema(query=Query)
