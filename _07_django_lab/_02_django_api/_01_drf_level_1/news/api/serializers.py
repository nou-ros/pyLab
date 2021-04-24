# ModelSerializer class workings

from rest_framework import serializers
from news.models import Article, Journalist

from datetime import datetime
from django.utils.timesince import timesince


class ArticleSerializers(serializers.ModelSerializer):

     # custom extra fields for serializers
    time_since_publication = serializers.SerializerMethodField()

    # calling the foreign key members' serializer - after creating the serializer
    # author = JournalistSerializer()
    '''
    this will show the foreign key field name instead of 
    id. before creating the foreign key field serializer.
    '''
    # author = serializers.StringRelatedField()

    class Meta:
        model = Article
        # fields = "__all__" #we want all the fields of our model
        # fields = ("title", "description", "body") # choose couple of fields
        exclude = ("id",) # excluded value will not be shown

    # custom extra fields for serializers function
    def get_time_since_publication(self, date_value):
        publication_date = date_value.publication_date
        now = datetime.now()
        time_delta = timesince(publication_date, now)
        return time_delta

    # custom validate method 
    def validate(self, data):
        # Check description and title are different
        
        if data["title"] == data["description"]:
            raise serializers.ValidationError("Title and description must be unique")
        return data
    
    def validate_title(self, value):
        
        # check title is more than 60 chars
        
        if len(value) < 60:
            raise serializers.ValidationError("Title must be longer than 60 chars")
        return value

# Jurnalist Serializer
class JournalistSerializer(serializers.ModelSerializer):
    
    # this will help to create journalist with articles.
    # articles = ArticleSerializers(many=True, read_only=True)

    # hyperlinked parameter, view_name is the end point 
    articles = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='article_detail')
     
    class Meta:
        model = Journalist
        fields = "__all__"

'''
# Serializer class workings 
from rest_framework import serializers
from news.models import Article

# work with Serializer class
class ArticleSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    author = serializers.CharField()
    title = serializers.CharField()
    description = serializers.CharField()
    body = serializers.CharField()
    location = serializers.CharField()
    publication_date = serializers.DateField()
    active = serializers.BooleanField()
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        print('created', validated_data)
        return Article.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        # we will send author to update 
        instance.author = validated_data.get('author', instance.author)
        # if no title found use the instance title with instance.title
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.body = validated_data.get('body', instance.body)
        instance.location = validated_data.get('location', instance.location)
        instance.publication_date = validated_data.get('publication_date', instance.publication_date)
        instance.active = validated_data.get('active', instance.active)
        instance.save()
        print('updated')
        return instance

    # custom validate method 
    def validate(self, data):
        # Check description and title are different
        
        if data["title"] == data["description"]:
            raise serializers.ValidationError("Title and description must be unique")
        return data
    
    def validate_title(self, value):
        
        # check title is more than 60 chars
        
        if len(value) < 60:
            raise serializers.ValidationError("Title must be longer than 60 chars")
        return value
    
    def validate_author(self, value):
        
        # author can't named admin
        
        if value == "admin":
            raise serializers.ValidationError("Author can't be named as admin")
        return value
'''