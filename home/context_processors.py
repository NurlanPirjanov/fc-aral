from .models import Gallery, OldMatch, Contact, News


def global_context(request):
    old_match = OldMatch.objects.last()
    contact = Contact.objects.last()
    gallery = Gallery.objects.order_by('-id')[:6]
    news = News.objects.order_by('-id')[:2]
    return {
        'contact': contact,
        'news':news,
        'gallery': gallery,
        'old_match': old_match,
        'site_name': 'PFK Aral',
        'logo_url': '/static/images/logo_pfk_aral.svg',
        'logo_url2': '/static/images/logo2.png',
        'logo_aral': '/static/images/SOCCER.png',
    }
