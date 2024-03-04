from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import BlogPost
from .serializers import BlogPostSerializer
from rest_framework.views import APIView

# Create your views here.
class BlogPostListCreate(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    
    def delete(self, request, *args, **kwargs):
        """
        Delete all blog posts.
        Parameters:
        request (Request): The request object.
        args (List): The list of arguments.
        kwargs (Dict): The dictionary of keyword arguments.
        """
        BlogPost.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class BlogPostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    lookup_field = "pk"

class BlogPostList(APIView):
    def get(self, request, format=None):
        """
        Get all blog posts.
        Parameters:
        request (Request): The request object.
        format (str): The format of the request.
        """
        title = request.query_params.get("title", None)
        
        if title:
            # filter blogposts by title
            blogposts = BlogPost.objects.filter(title__icontains=title)
        else:
            # if no title provided, return all blogposts
            blogposts = BlogPost.objects.all()
        
        serliazer = BlogPostSerializer(blogposts, many=True)
        return Response(serliazer.data, status=status.HTTP_200_OK)
     