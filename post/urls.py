from django.urls import path
from .views import *


urlpatterns = [
    path('categories/', CategoryView.as_view()),
    path('categories/<str:pk>/', CategoryDetailView.as_view()),
    path('tags/', TagView.as_view()),
    path('tags/<str:pk>/', TagDetailView.as_view()),
    path('posts/', PostView.as_view()),
    path('posts/<str:pk>/', PostDetailView.as_view()),
    ]

