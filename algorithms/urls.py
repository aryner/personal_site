from django.conf.urls import url
from algorithms import views

app_name = "algorithms"
urlpatterns = [
  url(r'^euclid/$',views.euclid,name='euclid')
]

