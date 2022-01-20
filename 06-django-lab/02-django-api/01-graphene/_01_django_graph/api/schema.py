import graphene

from graphene_django.types import DjangoObjectType

from .models import *

import graphql_jwt
from graphql_jwt.decorators import login_required

from graphene import relay
from graphene_django.filter import DjangoFilterConnectionField


# we will require separate field as id for relay mutation
from graphql_relay import from_global_id

# without relay approach
class MovieType(DjangoObjectType):
    class Meta:
        model = Movie

    # custom filed for a model, from graphql prespective. This will not generate any field in the model(database)
    movie_age = graphene.String()

    def resolve_movie_age(self, info):
        return "Old Movie" if self.year<2000 else "New Movie"

class DirectorType(DjangoObjectType):
    class Meta: 
        model = Director

# without relay approach
class Query(graphene.ObjectType):
    # for list of movies 
    all_movies = graphene.List(MovieType) 

    # for a single movie
    single_movie = graphene.Field(MovieType, id=graphene.Int(), title=graphene.String())

    # for list of all directors
    all_directors = graphene.List(DirectorType)

    # for both single and list of movies
    movie = graphene.List(MovieType, title = graphene.String())

    # without relay - we will require resolve
    # @login_required
    # resolve function for all movies
    def resolve_all_movies(self, info, **kwargs):
      # we can use this instead of login_required decorator
      # user = info.context.user
      # if not user.is_authenticated:
      #   raise Exception('Auth credentials were not provided')
      return Movie.objects.all()

    # resolve function for a single movie
    def resolve_single_movie(self, info, **kwargs):
        id = kwargs.get('id')
        title = kwargs.get('title')

        #query by id
        if id is not None:
            return Movie.objects.get(pk=id)

        # query by title
        if title is not None:
            return Movie.objects.get(title=title)
        
        return None

    # resolve function for all directors
    def resolve_all_directors(self, info, **kwargs):
        return Director.objects.all()
      
    # resolve for movie 
    def resolve_movie(self, info, **kwargs):
      title = kwargs.get('title')

      # query by title
      if title is not None:
        # send as list 
        return [Movie.objects.get(title=title)]

      else:
        return Movie.objects.all()



# # for relay
# class MovieNode(DjangoObjectType):
#   class Meta:
#     model = Movie
#     # filter_fields = ['title', 'year']
#     filter_fields = {
#       'title' : ['exact', 'icontains', 'istartswith'],
#       'year' : ['exact']

#     }

#     interfaces = (relay.Node, )


# # Releay version of Query
# class Query(graphene.ObjectType):
#   # all movies 
#   all_movies = DjangoFilterConnectionField(MovieNode)

#   # single movie
#   single_movie = relay.Node.Field(MovieNode)

'''
# everythin will work on graphqlView querySection

query{
  allMovies{
    id
    title
    year
    movieAge
    director{
      name
    }
  }
}

query{
  singleMovie(id: 1){
    title
    year
    movieAge
    director{
      name
    }
  }
}



#alias
query{
  firstMovie: singleMovie(id: 1){
    title
    year
    movieAge
    director{
      name
    }
  }
  
secondMovie: singleMovie(id: 2){
    title
    year
    movieAge
    director{
      name
    }
  }
}

# fragment
query{
  firstMovie: singleMovie(id: 1){
   ...movieData
  }
  
  secondMovie: singleMovie(id: 2){
 		...movieData
  }
}

# we can choose from here what to show and what not to show
fragment movieData on MovieType{
  id
  title
	year
  director{
    name
    surname
  }
}

# providing names to queries so we can select which queries to run

query MoviesAndDirector{

 	allMovies{
    title
    year
    director{
      surname
    }
  } 
}

query JustMovies{
 	allMovies{
    title
    year
  } 
}


# use of variables

query MovieAndDirector($id: Int){
  singleMovie(id: $id){
    id
    title
    year
    director{
      surname
    }
  }
}

# this will be used in Query Variables section to see the workings of - query MovieAndDirector($id: Int) - section

{
  "id":5
}


# directives are used to toggle a section. Use of directives
query MovieAndDirector($id:Int, $showDirector: Boolean = false){
  singleMovie(id: $id){
    id
    title
    year
    director @include(if: $showDirector){
      surname
    }
  }
}

# query variables section 
{
  "id":1,
  # if true then surname will show by default false
  "showDirector": true
}


'''


# Mutation
# create a movie
class MovieCreateMutation(graphene.Mutation):

  class Arguments:
    title = graphene.String(required=True)
    year = graphene.Int(required=True)

  movie = graphene.Field(MovieType)

  def mutate(self, info, title, year):
    movie = Movie.objects.create(title=title, year=year)

    return MovieCreateMutation(movie=movie)

# update a movie
class MovieUpdateMutation(graphene.Mutation):
  class Arguments:
    title = graphene.String()
    year = graphene.Int()
    id = graphene.ID(required=True)
  
  movie = graphene.Field(MovieType)

  def mutate(self, info, id, title, year):
    movie = Movie.objects.get(pk=id)

    if title is not None:
      movie.title = title
    if year is not None:
      movie.year = year
    movie.save()

    return MovieUpdateMutation(movie=movie)

# delete a movie
class MovieDeleteMutation(graphene.Mutation):
  class Arguments:
    id = graphene.ID(required=True)
  
  movie = graphene.Field(MovieType)

  def mutate(self, info, id):
    movie = Movie.objects.get(pk=id)
    movie.delete()

    return MovieDeleteMutation(movie=None)


# relay update mutation
class MovieUpdateMutationRelay(relay.ClientIDMutation):
  class Input:
    title = graphene.String()
    id = graphene.ID(required=True)
  
  movie = graphene.Field(MovieType)

  @classmethod
  def mutate_and_get_payload(cls, root, info, id, title):
    movie = Movie.objects.get(pk=from_global_id(id)[1])

    if title is not None:
      movie.title = title

    movie.save()

    return MovieUpdateMutationRelay(movie=movie)

class Mutation:
  # for authentication
  # token_auth = graphql_jwt.ObtainJSONWebToken.Field()
  # verify_token = graphql_jwt.Verify.Field()
  # refresh_token = graphql_jwt.Refresh.Field()

  create_movie = MovieCreateMutation.Field()
  update_movie = MovieUpdateMutation.Field()
  delete_movie = MovieDeleteMutation.Field()

  update_movie_relay = MovieUpdateMutationRelay.Field()



"""
mutation createMovie{
  createMovie(title:"Howl's Movie Castle", year:2004)
  {
    movie{
      id
      title
     	year
      movieAge
    }
  }
}
mutation updateMovie{
  updateMovie(id: 4, title:"Sprited", year:2002)
  {
    movie{
      id
      title
     	year
      movieAge
    }
  }
}

mutation deleteMovie{
  deleteMovie(id: 5)
  {
    movie{
      id
    }
  }
}

query AllMovies{
  allMovies{
    id
    title
    year
  }
}
"""

# token
"""
mutation GetToken{
  tokenAuth(username:"admin", password:"admin")
  {
    token
  }
}

query AllMovies{
  allMovies{
    title
  }
}

mutation VerifyToken{
  verifyToken(token: "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNjAwNTIxNTU5LCJvcmlnSWF0IjoxNjAwNTIxMjU5fQ.2CgWMM1r2CUFNvf5F7o_coeNhCkhP1IPuKijs7oK-hM")
  {
    payload
  }
}

"""

"""
# relay query

query AllMovies{
  allMovies{
  	edges{
      node{
        id
        title
        year
        director{
          id
          name 
          surname
        }
      }
    }
  }
}


query singleMovie{
  singleMovie(id: "TW92aWVOb2RlOjI=")
  {
    title
    year
  }
}

# with exclusive filter option
- icontains

query AllMovies{
	allMovies(title_Icontains:"T"){
    edges{
      node{
        id
        title
        year
      }
    }
  }  
}

-istartswith
query AllMovies{
	allMovies(title_Istartswith:"T"){
    edges{
      node{
        id
        title
        year
      }
    }
  }  
}


relay mutation

mutation MutateRelay{
  updateMovieRelay(
    input: {id: "TW92aWVOb2RlOjI=", title: "Avatar"}
  ){
    movie{
      id
      title
      year
    }
  }
}

# limiting records -> pagination

query AllMovies{
	allMovies(first: 10){
    edges{
      node{
        id
        title
        year
      }
    }
  }  
}



query AllMovies{
	allMovies(first: 3){
    pageInfo{
      startCursor
      endCursor
      hasNextPage
      hasPreviousPage
    }
    edges{
      cursor
      node{
        id
        title
        year
      }
    }
  }  
}

query AllMovies{
	allMovies(first: 1, after:"YXJyYXljb25uZWN0aW9uOjE="){
    pageInfo{
      startCursor
      endCursor
      hasNextPage
      hasPreviousPage
    }
    edges{
      cursor
      node{
        id
        title
        year
      }
    }
  }  
}

"""