from tools.formatJsonNotes import format_content
from tools.notesToJson import getLines, transformToJson

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','personal_site.settings')

import django
django.setup()

from blog.models import Post, Speaker, Location, Event

if __name__ == '__main__':
  import sys

  if len(sys.argv) < 2):
    print('You must enter the notes file path as a command line arguement')
    sys.exit()

  lines = getLines(sys.argv[1]) 
