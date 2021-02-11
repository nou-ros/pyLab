#general schema file. It will help to reference other app's schema files
import graphene
import tracks.schema


class Query(tracks.schema.Query, graphene.ObjectType):
    pass



class Mutation(tracks.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation) 