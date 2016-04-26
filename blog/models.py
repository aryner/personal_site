from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

class Post(models.Model):
  title = models.CharField(max_length=128,unique=True,primary_key=True)
  title_link = models.URLField()
  subtitle = models.CharField(max_length=128)
  date = models.DateField()
  content = models.TextField()
  published = models.BooleanField(default='False')
  slug = models.SlugField(default='')

  def save(self,*args,**kwargs):
    self.slug = slugify(self.title)
    super(Post, self).save(*args, **kwargs)

  def __str__(self):
    return self.title

class Speaker(models.Model):
  name = models.CharField(max_length=128,unique=True)
  link = models.URLField()
  posts = models.ManyToManyField(Post)

  def __str__(self):
    return self.name

class Location(models.Model):
  name = models.CharField(max_length=128,unique=True)
  link = models.URLField()
  posts = models.ManyToManyField(Post)

  def __str__(self):
    return self.name

class Comment(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  post = models.ManyToManyField(Post)
  content = models.TextField()
  dateTime = models.DateTimeField(auto_now_add=True)
  root_comment = models.BooleanField(default=True)
  children = models.ManyToManyField('Comment')

  def __str__(self):
    return '%s: %s'%(self.user.username,self.content[0:20])
