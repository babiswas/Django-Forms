from django.urls import path,include
from .views import add_blog,blog_detail


app_name='Blog'

urlpatterns = [
    path('add_blog/',add_blog, name='add_blog'),
    path('blog_detail/',blog_detail, name='blog_detail'),
]