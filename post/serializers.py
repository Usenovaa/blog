from rest_framework.serializers import Serializer, ModelSerializer
from .models import Category, Tag, Post



class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class PostListSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'slug', 'image')