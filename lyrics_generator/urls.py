from django.urls import path
# from django.conf.urls import url, include
from . import views

# app_name = 'lyrics_generator'

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('search', views.search, name='search'),
    path('lyrics_response', views.lyrics, name='lyrics'),
    path('timeline', views.timeline, name = 'timeline')
]
