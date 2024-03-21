from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *


router = DefaultRouter()
router.register('posts', PostViewset)
router.register('comments', CommentViewset)
router.register('like', LikeViewset)


urlpatterns = [
    path('categories/', CategoryView.as_view()),
    path('categories/<str:pk>/', CategoryDetailView.as_view()),
    path('tags/', TagView.as_view()),
    path('tags/<str:pk>/', TagDetailView.as_view()),
    path('', include(router.urls))
    # path('posts/', PostViewset.as_view({'get': 'list', 'post': 'create'})),
    # path('posts/<str:pk>/', PostViewset.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})),
    ]

