from django.urls import path
from . import views

urlpaterns = [
    path("blogposts/", views.BlogPostListCreate.as_view(), name="blogpost-list-create"),
]