from django.apps import AppConfig
from subprocess import call

class BlogConfig(AppConfig):
    name = 'blog'
    def read(self):
      call(["python","manage.py","makemigrations"])
      call(["python","manage.py","migrate"])
