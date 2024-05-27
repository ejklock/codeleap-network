from django.contrib import admin
from django.urls import path

from .domains.post.views import PostDetail, PostList

urlpatterns = [
    path('posts/', PostList().as_view()),
    path('posts/<int:pk>/', PostDetail().as_view()),
]
