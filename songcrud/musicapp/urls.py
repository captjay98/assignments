from django.urls import path
from . import  views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('artistes/', views.get_artiste),
    path('songs/', views.get_song),
    path('lyrics/', views.get_lyric),
    path('artistes/<int:id>', views.artiste_detail),
    path('songs/<int:id>', views.song_detail),
    path('lyrics/<int:id>', views.lyric_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)