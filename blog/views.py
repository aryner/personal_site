import datetime

from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from blog.models import Post, Speaker, Location, Comment

# Create your views here.
def index(request):
  posts = Post.objects.order_by('date')[:5]
  base_context = {'posts':posts}

  return render(request,'blog/index.html',base_context)

def post(request,title_slug):
  post = Post.objects.get(slug=title_slug)
  speakers = Speaker.objects.all().filter(posts=post)
  location = Location.objects.all().filter(posts=post)[0]
  comments = Comment.objects.all().filter(post=post)

  base_context = {'post':post,'speakers':speakers,'location':location,'comments':comments}
  return render(request,'blog/post.html',base_context)

@login_required
def comment(request):
  post_slug = request.POST.get('post_slug')
  if request.method == 'POST':
    content = request.POST.get('comment')
    if content:
      posted_to = Post.objects.all().filter(slug=post_slug)[0]
      parent = request.POST.get('parent')
      parent = None if int(parent) < 0 else Comment.objects.all().filter(id=int(parent))[0]
      comment = Comment.objects.create(user=request.user,
                                       content=content,
                                       dateTime=datetime.datetime.now(),
                                       parent=parent)
      comment.post.add(posted_to)
      comment.save()

    return post(request,post_slug)

  return index(request)

