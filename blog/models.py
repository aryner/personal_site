from django.db import models

class Post(models.Model):
  title = models.CharField(max_length=128,unique=True,primary_key=True)
  title_link = models.URLField()
  subtitle = models.CharField(max_length=128)
  date = models.DateField()
  content = models.TextField()

class Speaker(models.Model):
  name = models.CharField(max_length=128,unique=True)
  link = models.URLField()
  posts = models.ManyToManyField(Post)

class Location(models.Model):
  name = models.CharField(max_length=128,unique=True)
  link = models.URLField()
  posts = models.ManyToManyField(Post)

class Event(models.Model):
  name = models.CharField(max_length=128,unique=True)
  link = models.URLField()
  posts = models.ManyToManyField(Post)
  

