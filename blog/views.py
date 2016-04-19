from django.http import HttpResponse
from django.shortcuts import render

from blog.models import Post, Speaker, Location

# Create your views here.
def index(request):
  posts = Post.objects.order_by('date')[:5]
  base_context = {'posts':posts}

  return render(request,'blog/index.html',base_context)

def post(request,title_slug):
  post = Post.objects.get(slug=title_slug)
  speakers = Speaker.objects.all().filter(posts=post)
  location = Location.objects.all().filter(posts=post)[0]

  base_context = {'post':post,'speakers':speakers,'location':location}
  return render(request,'blog/post.html',base_context)

