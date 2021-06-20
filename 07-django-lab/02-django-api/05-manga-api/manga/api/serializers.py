from rest_framework import serializers
from manga.models import MangaAuthor, Mangas, Review


class MangaAuthorSerializer(serializers.ModelSerializer):
    avatar = serializers.ImageField(read_only=True)

    class Meta:
        model = MangaAuthor
        fields = '__all__'


class MangaAuthorAvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = MangaAuthor
        fields = ('avatar',)


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        exclude = ('manga',)


class MangaSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)
    image = serializers.ImageField(read_only=True)

    class Meta:
        model = Mangas
        fields = '__all__'


class MangaImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mangas
        fields = ('image',)
