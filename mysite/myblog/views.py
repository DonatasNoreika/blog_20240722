from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here.
class PostListView(generic.ListView):
    model = Post
    template_name = "index.html"
    context_object_name = "posts"

