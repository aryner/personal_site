from django.contrib import admin
from blog.models import Post, Speaker, Location, Event

# Register your models here.
admin.site.register(Post)
admin.site.register(Speaker)
admin.site.register(Location)
admin.site.register(Event)
