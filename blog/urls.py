from django.conf.urls import url
from blog import views

app_name = 'blog'
urlpatterns = [
  url(r'^$',views.index,name='index'),
  url(r'^comment/$',views.comment,name='comment'),
  url(r'^post/(?P<title_slug>[\w\-]+)/$',views.post,name='post'),
  url(r'^preview_post/(?P<title_slug>[\w\-]+)/$',views.preview_post,name='preview_post'),
  url(r'^manage_posts/$',views.manage_posts,name='manage_posts'),
  url(r'^add_post/$',views.add_post,name='add_post'),
  url(r'^publish/(?P<title_slug>[\w\-]+)/$',views.publish,name='publish'),
  url(r'^unpublish/(?P<title_slug>[\w\-]+)/$',views.unpublish,name='unpublish'),
  url(r'^delete_post/(?P<title_slug>[\w\-]+)/$',views.delete_post,name='delete_post'),
]

