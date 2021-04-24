#work with API_View
from rest_framework.views import APIView
from news.models import Article, Journalist
from news.api.serializers import ArticleSerializers, JournalistSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404

# most functionality will remain same 
class ArticleListCreaetAPIView(APIView):
    def get(self, request):
        articles = Article.objects.filter(active=True)
        serializer = ArticleSerializers(articles, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ArticleSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class ArticleDetailApiView(APIView):
    
    def get_object(self, pk):
        article = get_object_or_404(Article, pk=pk)
        return article 
    
    def get(self, request, pk):
        article = self.get_object(pk)
        serializer = ArticleSerializers(article)
        return Response(serializer.data)

    def put(self, request, pk):
        article = self.get_object(pk)
        serializer = ArticleSerializers(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        article = self.get_object(pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# journalist api view 
class JournalistListCreateAPIView(APIView):
    def get(self, request):
        journalists = Journalist.objects.all()
        # if we use hyperlinked field then we have use context 
        serializer = JournalistSerializer(journalists, many=True, context={'request':request})
        return Response(serializer.data)
    
    def post(self, request):
        serializer = JournalistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

'''
#work with @api_view
from rest_framework.decorators import api_view
from news.models import Article
from news.api.serializers import ArticleSerializers
from rest_framework.response import Response
from rest_framework import status

# both list all articles and will be able to create article
@api_view(["GET", "POST"])
def article_list_create_api_view(request):

    # to list
    if request.method == "GET":
        articles = Article.objects.filter(active=True)
        # feed the article to serializer
        # many=True will make sure to load full queryset
        serializer = ArticleSerializers(articles, many=True)
        return Response(serializer.data)

    # to create 
    elif request.method == "POST":
        # request.data = posted data
        serializer = ArticleSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#detail api view 
@api_view(["GET", "PUT", "DELETE"])
def article_detail_api_view(request, pk):
    # check if the article exist with custom try except we can use get_object_or_404 too.
    try:
        article = Article.objects.get(pk=pk)

    except Article.DoesNotExist:
        return Response({
            "error": {
                "code": 404,
                "message": "Article not found",
            }
        }, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = ArticleSerializers(article)
        return Response(serializer.data)
    
    elif request.method == "PUT":
        serializer = ArticleSerializers(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "DELETE":
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
'''