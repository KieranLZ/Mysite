#This one is in blogs

from django.urls import path, include, re_path

from . import views

urlpatterns = [
    re_path('^$', views.index, name='index')
]

app_name = 'blogs'