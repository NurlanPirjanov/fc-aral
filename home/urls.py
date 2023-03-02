from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='HomePage'),
    path('matches/', MatchView, name='MatchPage'),
    path('players/', PlayerView, name='PlayersPage'),
    path('news/', NewsView, name='NewsPage'),
    path('contact/', ContactView, name='ContactPage'),
    path('news/<int:pk>/', DetailView, name='DetailPage'),
    path('news/com_add/<int:pk>/', add_comment, name='add_comment'),
    path('next/', LangView, name="lang_url"),
]