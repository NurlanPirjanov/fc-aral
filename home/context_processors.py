from .models import Gallery, OldMatch, Contact


def global_context(request):
    old_match = OldMatch.objects.last()
    contact = Contact.objects.last()
    gallery = Gallery.objects.order_by('-id')[:6]
    return {
        'contact': contact,
        'gallery': gallery,
        'old_match': old_match,
        'site_name': 'PFK Aral',
        'logo_url': '/static/images/logo_pfk_aral.svg',
        'logo_url2': '/static/images/logo2.png',
        'logo_aral': '/static/images/SOCCER.png',
    }
