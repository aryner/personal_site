from django.contrib import admin
from blog.models import Post, Speaker, Location, Comment

admin.site.register(Post)
admin.site.register(Speaker)
admin.site.register(Location)
admin.site.register(Comment)
