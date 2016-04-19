from tools.formatJsonNotes import format_content
from tools.notesToJson import getLines, transformToJson

import datetime
import sys
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','personal_site.settings')

import django
django.setup()

from blog.models import Post, Speaker, Location, Event

def add_post(file_name):
  lines = getLines(file_name) 
  json = transformToJson(lines)
  content = format_content(json)

  if Post.objects.all().filter(title=json['title']):
    print('Unable to add %s as it already exists'%json['title'],file=sys.stderr)
    return

  post = Post.objects.get_or_create(title = json['title'],
                                    title_link = json['title_link'],
                                    subtitle = json['subtitle'],
                                    date = datetime.datetime.now(),
                                    content = content)[0]
  post.save()

if __name__ == '__main__':
  if len(sys.argv) < 2:
    print('You must enter the notes file path as a command line arguement')
    sys.exit()

  add_post(sys.argv[1])

