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


def home(request):
    next_match = NextMatch.objects.last()
    news = News.objects.order_by('-id')[:3]
    liga = Liga.objects.latest('id')
    gallery = Gallery.objects.order_by('-id')[:6]
    context = {
        'next_match': next_match,
        'news': news,
        'liga': liga,
        'gallery':gallery,
    }
    return TemplateResponse(request, "home/index.html", context)


def MatchView(request):
    next_match = NextMatch.objects.last()
    news = News.objects.order_by('-id')[:2]
    old_matches = OldMatch.objects.all()
    paginator = Paginator(old_matches, 9)
    page_number = request.GET.get('page')
    match_obj = paginator.get_page(page_number)
    context = {
        'match_obj':match_obj,
        'next_match': next_match,
        'news':news,
    }
    return TemplateResponse(request, "home/matches.html", context)


def LangView(request):
    lang_url = request.GET.get("lang")
    next_url = request.GET.get("url")[4:]
    full_url = f'/{lang_url}/{next_url}'
    return redirect(full_url)


def DetailView(request, pk):
    articles = News.objects.all()
    random_article = random.choice(articles)
    article = get_object_or_404(News, pk=pk)
    form = CommentForm()
    context = {'article': article,
               'random_article':random_article,
               'form': form,
               }
    return render(request, 'home/article_detail.html', context)


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
    news = News.objects.order_by('-id')[:2]
    context = {
        'news': news,
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
