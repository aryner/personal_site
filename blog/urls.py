from django.conf.urls import url
from blog import views

app_name = 'blog'
urlpatterns = [
  url(r'^$',views.index,name='index'),
  url(r'^post$',views.post,name='post'),
]

