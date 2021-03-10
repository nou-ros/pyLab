from datetime import datetime
from django.utils.timesince import timesince

from rest_framework import serializers
from news.models import Article, Journalist


# 2. working with ModelSerializer
class ArticleSerializer(serializers.ModelSerializer):

    # extra filed for serializer
    time_since_publication = serializers.SerializerMethodField()
    # represent the author as string
    # author = serializers.StringRelatedField()
    # author = JournalistSerializer()

    class Meta:
        model = Article
        #fields = "__all__" # we want all the fields
        # fields = ("title", "description", "body") # we want specific fields
        exclude = ("id", )

    # extra filed for serializer
        # object is instance here
    def get_time_since_publication(self, object):
        publication_date = object.publication_date
        now = datetime.now()
        time_delta = timesince(publication_date, now)
        return time_delta

    #custom validation same as Serializer
    #validate for same title and description
    def validate(self, data):
        # check that description and title are different

        if data["title"] == data["description"]:
            raise serializers.ValidationError("Title and description must be different.")
        return data
    
    #validate title with more than 60 chars
    def validate_title(self, value):
        if len(value)<30:
            raise serializers.ValidationError("Title has to be 30 characters.")
        return value

# working with journalist serializer
class JournalistSerializer(serializers.ModelSerializer):
    # article will be shown as a link to another page
    article_author = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name="article-detail")
    # articles on the listed page
    # article_author = ArticleSerializer(many=True, read_only=True)

    class Meta:
        model = Journalist
        fields = "__all__"


# 1. working with Serializer
'''
class ArticleSerializer(serializers.Serializer):
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
        print(validated_data)
        return Article.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.author = validated_data.get('author' or instance.author)
        instance.title = validated_data.get('title' or instance.title)
        instance.description = validated_data.get('description' or instance.description)
        instance.body = validated_data.get('body' or instance.body)
        instance.location = validated_data.get('location' or instance.location)
        instance.publication_date = validated_data.get('publication_date' or instance.publication_date)
        instance.active = validated_data.get('active' or instance.active)
        instance.save()
        return instance

    #custom validation
    #validate for same title and description
    def validate(self, data):
        # check that description and title are different

        if data["title"] == data["description"]:
            raise serializers.ValidationError("Title and description must be different.")
        return data
    
    #validate title with more than 60 chars
    def validate_title(self, value):
        if len(value)<60:
            raise serializers.ValidationError("Title has to be 60 characters.")
        return value
'''