from tools.formatJsonNotes import format_content
from tools.notesToJson import getLines, transformToJson

import datetime
import sys
from blog.models import Post, Speaker, Location

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
                                    content = content,
                                    published = False)[0]
  post.save()

  speakers = json['speakers']
  i = 1
  while str(i) in speakers:
    speaker = Speaker.objects.get_or_create(name=speakers[str(i)])[0]
    speaker.link = speakers['%d_link'%i]
    speaker.posts.add(post)
    speaker.save()
    i += 1

  location = Location.objects.get_or_create(name=json['location'])[0]
  location.link = json['location_link']
  location.posts.add(post)
  location.save()

if __name__ == '__main__':
  import os
  os.environ.setdefault('DJANGO_SETTINGS_MODULE','personal_site.settings')
  import django
  django.setup()

  if len(sys.argv) < 2:
    print('You must enter the notes file path as a command line arguement')
    sys.exit()

  add_post(sys.argv[1])

