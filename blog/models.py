from django.db import models

def Post(models.Model):
  title = models.CharField(max_length=128,unique=True)
  title_link = models.URLField()
  subtitle = models.CharField(max_length=128)
  date = models.DateField()
  content = models.TextField()

def Speaker(models.Model):
  name = models.CharField(max_length=128,unique=True)
  link = models.URLField()
  posts = models.ManyToManyField(Post)

def Location(models.Model):
  name = models.CharField(max_length=128,unique=True)
  link = models.URLField()
  posts = models.ManyToManyField(Post)

def Event(models.Model):
  name = models.CharField(max_length=128,unique=True)
  link = models.URLField()
  posts = models.ManyToManyField(Post)
  

