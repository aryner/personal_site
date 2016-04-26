import datetime

from django.http import HttpResponse, HttpResponseRedirect
from django.conf.urls import url
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User

from blog.models import Post, Speaker, Location, Comment
from manage_posts import add_post as load_post

def index(request):
  posts = Post.objects.all().filter(published=True).order_by('-date')[:5]
  base_context = {'posts':posts}

  return render(request,'blog/index.html',base_context)

def post(request,title_slug):
  post = Post.objects.get(slug=title_slug)
  speakers = Speaker.objects.all().filter(posts=post)
  location = Location.objects.all().filter(posts=post)[0]
  comments = Comment.objects.all().filter(post=post).filter(root_comment=True)

  base_context = {'post':post,'speakers':speakers,'location':location,'comments':comments}
  return render(request,'blog/post.html',base_context)

@login_required
def preview_post(request,title_slug):
  if not request.user.is_superuser:
    return HttpResponseRedirect('/blog/')

  post = Post.objects.get(slug=title_slug)
  speakers = Speaker.objects.all().filter(posts=post)
  location = Location.objects.all().filter(posts=post)[0]
  comments = Comment.objects.all().filter(post=post).filter(root_comment=True)

  base_context = {'post':post,'speakers':speakers,'location':location,'comments':comments}
  return render(request,'blog/preview_post.html',base_context)

@login_required
def publish(request,title_slug):
  if not request.user.is_superuser:
    return HttpResponseRedirect('/blog/')

  post = Post.objects.get(slug=title_slug)
  post.published = True
  post.save()
  return HttpResponseRedirect('/blog/manage_posts')

@login_required
def unpublish(request,title_slug):
  if not request.user.is_superuser:
    return HttpResponseRedirect('/blog/')

  post = Post.objects.get(slug=title_slug)
  post.published = False
  post.save()
  return HttpResponseRedirect('/blog/manage_posts')
  
@login_required
def delete_post(request,title_slug):
  if not request.user.is_superuser:
    return HttpResponseRedirect('/blog/')

  post = Post.objects.get(slug=title_slug)
  post.delete()
  return HttpResponseRedirect('/blog/manage_posts')

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
                                       root_comment=(parent==None))
      comment.post.add(posted_to)
      comment.save()

      if parent:
        parent.children.add(comment)
        parent.save()

    return HttpResponseRedirect('/blog/post/%s/'%posted_to.slug)

  return index(request)

@login_required
def manage_posts(request):
  if request.user.is_superuser:
    posts = Post.objects.order_by('-date')
    base_context = {'posts':posts}
    return render(request, 'blog/manage_posts.html',base_context)
  else:
    return HttpResponseRedirect('/blog/')

@login_required
def add_post(request):
  if request.user.is_superuser and request.method == 'POST':
    if request.FILES:
      new_post = request.FILES['raw_post']
      load_post(new_post)
    return HttpResponseRedirect('/blog/manage_posts')
  else:
    return HttpResponseRedirect('/blog/')


