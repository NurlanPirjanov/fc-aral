from datetime import date
from django.http import HttpResponse
from django.template import loader
from django.template.response import TemplateResponse
from .models import *
from django.core.paginator import Paginator
from django.views.generic.detail import DetailView
import random
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .forms import CommentForm
from django.shortcuts import redirect
from django.views.generic import TemplateView
from hitcount.views import HitCountDetailView
def home(request):
    next_match = NextMatch.objects.last()
    liga = Liga.objects.latest('id')
    gallery = Gallery.objects.order_by('-id')[:6]
    news3 = News.objects.order_by('-id')[:3]
    context = {
        'next_match': next_match,
        'liga': liga,
        'gallery':gallery,
        'news3':news3,
    }
    return TemplateResponse(request, "home/index.html", context)


def RahbariyatView(request):
    rahb = Rahbariyat.objects.all()
    context = {
        'rahb':rahb,
    }
    return TemplateResponse(request, "home/rahbariyat.html", context)


def TrenerView(request):
    trener = Trener.objects.all()
    context = {
        'trener':trener,
    }
    return TemplateResponse(request, "home/trener.html", context)


def U19View(request):
    object = U19.objects.first()
    context = {
        'object':object,
    }
    return TemplateResponse(request, "home/other_page.html", context)

def historyView(request):
    object = ClubHistory.objects.first()
    context = {
        'object':object,
    }
    return TemplateResponse(request, "home/other_page.html", context)

def stadionView(request):
    object = Stadion.objects.first()
    context = {
        'object':object,
    }
    return TemplateResponse(request, "home/other_page.html", context)

def mediatekaPage(request):
    object = Gallery.objects.all()
    items_per_page = 18
    paginator = Paginator(object, items_per_page)
    page_number = request.GET.get('page')
    news_obj = paginator.get_page(page_number)
    context = {
        'object':object,
        'news_obj': news_obj,
    }
    return TemplateResponse(request, "home/media.html", context)


def MatchView(request):
    next_match = NextMatch.objects.last()
    old_matches = OldMatch.objects.all()
    paginator = Paginator(old_matches, 9)
    page_number = request.GET.get('page')
    match_obj = paginator.get_page(page_number)
    context = {
        'match_obj':match_obj,
        'next_match': next_match,
    }
    return TemplateResponse(request, "home/matches.html", context)

def MatchDetailView(request, pk):
    old_matches = get_object_or_404(OldMatch, pk=pk)
    context = {
        'object': old_matches,
    }
    return TemplateResponse(request, "home/match_detail.html", context)

def LangView(request):
    lang_url = request.GET.get("lang")
    next_url = request.GET.get("url")[4:]
    full_url = f'/{lang_url}/{next_url}'
    return redirect(full_url)

def LigaDetailView(request, pk):
    liga = get_object_or_404(Liga, pk=pk)
    context = {
        'liga': liga,
    }
    return TemplateResponse(request, "home/liga_detail.html", context)


class DetailView(HitCountDetailView):
    model = News
    template_name = 'home/article_detail.html'
    count_hit = True
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        articles = News.objects.all()
        random_article = random.choice(articles)
        article = get_object_or_404(News, pk=self.kwargs.get('pk'))
        form = CommentForm()
        context['article'] = article
        context['random_article'] = random_article
        context['form'] = form
        return context

def add_comment(request, pk):
    news = News.objects.get(pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.news = news
            comment.save()
            return redirect('DetailPage', pk=news.pk)
    else:
        form = CommentForm()
    return render(request, 'add_comment.html', {'form': form, 'news': news})


def PlayerView(request):
    player = Player.objects.all()
    context = {
        'players':player
    }
    return TemplateResponse(request, "home/players.html", context)


def NewsView(request):
    news = News.objects.all()
    items_per_page = 9
    paginator = Paginator(news, items_per_page)
    page_number = request.GET.get('page')
    news_obj = paginator.get_page(page_number)
    context = {
        'news_obj': news_obj,
    }
    return TemplateResponse(request, "home/news.html", context)


def ContactView(request):
    return TemplateResponse(request, "home/contact.html")
