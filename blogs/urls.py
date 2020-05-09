#This one is in blogs

from django.urls import path, include, re_path

from . import views

urlpatterns = [
    re_path('^$', views.index, name='index'),
    re_path(r'^topics/$',views.topics,name='topics'),
    re_path(r'^topics/(?P<topic_id>\d+)/$', views.topic,name='topic')
]

app_name = 'blogs'