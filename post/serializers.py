from rest_framework.serializers import Serializer, ModelSerializer, ReadOnlyField
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
    author = ReadOnlyField(source='author.email')

    class Meta:
        model = Post
        fields = '__all__'
        
    def create(self, validated_data):
        user = self.context.get('request').user
        validated_data['author'] = user
        return super().create(validated_data)


class PostListSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'slug', 'image')