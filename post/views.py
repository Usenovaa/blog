import datetime
from rest_framework import generics, viewsets
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated, AllowAny

from .permissions import IsAuthorPermission
from .serializers import *
from .models import Category



# class CategoryCreateView(CreateAPIView):
#     serializer_class = CategorySerializer
#     # queryset = Category.objects.all()


class CategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)
        return Response('Successfully deleted ')


class TagView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


# class PostView(generics.ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     filter_backends = [DjangoFilterBackend, SearchFilter]
#     filterset_fields = ['category', 'tags__slug', 'title']
#     search_fields = ['title', 'body']

#     def get_serializer_class(self):
#         if self.request.method == 'GET':
#             return PostListSerializer
#         return self.serializer_class
#         # return PostSerializer
    

# class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
    

class PostViewset(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['category', 'tags__slug', 'title']
    search_fields = ['title', 'body']
    
    def get_serializer_class(self):
        if self.action == 'list':
            return PostListSerializer
        return self.serializer_class
    
    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [IsAuthenticated]
        elif self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAuthorPermission]
        return super().get_permissions()

        



