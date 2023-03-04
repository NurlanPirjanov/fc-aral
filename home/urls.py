from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='HomePage'),
    path('matches/', MatchView, name='MatchPage'),
    path('players/', PlayerView, name='PlayersPage'),
    path('news/', NewsView, name='NewsPage'),
    path('contact/', ContactView, name='ContactPage'),
    path('news/<int:pk>/', DetailView.as_view(), name='DetailPage'),
    path('news/com_add/<int:pk>/', add_comment, name='add_comment'),
    path('next/', LangView, name="lang_url"),
    path('liga/<int:pk>/',LigaDetailView, name="liga_detail"),
    path('rahbariyat/', RahbariyatView, name="rahbariyat"),
    path('trener/', TrenerView, name="trener"),
    path('U-19/', U19View, name="U19"),
    path('history/', historyView, name="history"),
    path('stadion/', stadionView, name="stadion"),
    path('media/', mediatekaPage, name="mediateka"),
]