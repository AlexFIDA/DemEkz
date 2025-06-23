from django.contrib import admin
from django.urls import path, include
from blog.views import *
from blog import views

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('blog/', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]
