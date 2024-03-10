from django.shortcuts import render
from rest_framework import generics
from .serializer import BlogSerializer
from .models import Blog
# Create your views here.


class BlogListView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
