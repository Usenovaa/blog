from rest_framework.serializers import Serializer, ModelSerializer, ReadOnlyField
from .models import Category, Tag, Post, Comment, Like


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
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['likes'] = instance.likes.count()
        # representation['comments'] = CommentSerializer(instance.comments.all(), many=True).data
        representation['comments'] = [i.body for i in instance.comments.all()]
        return representation


class PostListSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'slug', 'image')


class CommentSerializer(ModelSerializer):
    author = ReadOnlyField(source='author.email')

    class Meta:
        model = Comment
        fields = '__all__'

    def create(self, validated_data):
        user = self.context.get('request').user
        validated_data['author'] = user
        return super().create(validated_data)
       

class LikeSerializer(ModelSerializer):
    author = ReadOnlyField(source='author.email')

    class Meta:
        model = Like
        fields = '__all__'

    def create(self, validated_data):
        user = self.context.get('request').user
        validated_data['author'] = user
        return super().create(validated_data)