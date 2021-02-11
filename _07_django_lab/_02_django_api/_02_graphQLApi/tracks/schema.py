import graphene
from graphene_django import DjangoObjectType

from .models import Track

class TrackType(DjangoObjectType):
    class Meta:
        model = Track


class Query(graphene.ObjectType):
    tracks = graphene.List(TrackType)

    def resolve_tracks(self, info):
        return Track.objects.all()


class CreateTrack(graphene.Mutation):
    track = graphene.Field(TrackType)

    class Arguments: 
        title = graphene.String()
        desc = graphene.String()
        url = graphene.String()

    #a way to mutate
    # def mutate(self, info, **kwargs):
    #     kwargs.get('title')

    #another way to mutate
    def mutate(self, info, title, desc, url):
        track = Track(title=title, desc=desc, url=url)
        track.save()
        return CreateTrack(track=track)


class Mutation(graphene.ObjectType):
    create_track = CreateTrack.Field()