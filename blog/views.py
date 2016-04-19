from django.http import HttpResponse
from django.shortcuts import render

from blog.models import Post, Speaker, Location

# Create your views here.
def index(request):
  posts = Post.objects.order_by('date')[:5]
  base_context = {'posts':posts}

  return render(request,'blog/index.html',base_context)

def post(request):
  return render(request,'blog/post.html',{})

