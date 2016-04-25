from django.conf.urls import url
from blog import views

app_name = 'blog'
urlpatterns = [
  url(r'^$',views.index,name='index'),
  url(r'^comment/$',views.comment,name='comment'),
  url(r'^post/(?P<title_slug>[\w\-]+)/$',views.post,name='post'),
  url(r'^manage_posts/$',views.manage_posts,name='manage_posts'),
]

