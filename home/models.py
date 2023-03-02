from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class LogoFc(models.Model):
    name = models.CharField(max_length=100, verbose_name="Kamanda atı")
    img = models.ImageField(upload_to='images/logo/', verbose_name='Kamanda logosı')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Kamanda logotipi"
        verbose_name_plural = "Kamanda logotipleri"

class OldMatch(models.Model):
    """Bas bet - Aldınǵı oyın"""
    league = models.CharField(max_length=150, verbose_name="Liga atı")
    kamanda1 = models.CharField(max_length=50, verbose_name="1-kamanda")
    kamanda1_image = models.ForeignKey(LogoFc, on_delete=models.CASCADE, related_name="kam1")
    sk1 = models.IntegerField(verbose_name="1-kamanda gollar")
    kamanda2 = models.CharField(max_length=50, verbose_name="2-kamanda")
    kamanda2_image = models.ForeignKey(LogoFc, on_delete=models.CASCADE, related_name="kam2")
    sk2 = models.IntegerField(verbose_name="2-kamanda gollar")
    date = models.DateField(verbose_name='Oqın waqtı (sáne)')
    time = models.CharField(max_length=25, verbose_name='Oqın waqtı (saat)', default='15:00 GMT+5')
    active = models.BooleanField(verbose_name='Aktiv', default=True)

    def __str__(self):
        return f'{self.kamanda1} vs {self.kamanda2}'

    class Meta:
        verbose_name = 'Aldınǵı oyın'
        verbose_name_plural = 'Aldınǵı oyınlar'


class NextMatch(models.Model):
    """Bas bet - Kelesi oyın"""
    league = models.CharField(max_length=150, verbose_name="Liga atı")
    kamanda1 = models.CharField(max_length=50, verbose_name="1-kamanda")
    kamanda1_image = models.ForeignKey(LogoFc, on_delete=models.CASCADE,related_name="nextkam1")
    kamanda2 = models.CharField(max_length=50, verbose_name="2-kamanda")
    kamanda2_image = models.ForeignKey(LogoFc, on_delete=models.CASCADE, related_name="nextkam2")
    date = models.DateField(verbose_name='Oqın waqtı (sáne)')
    time = models.CharField(max_length=25, verbose_name='Oqın waqtı (saat)', default='15:00 GMT+5')
    active = models.BooleanField(verbose_name='Aktiv', default=True)

    def __str__(self):
        return f'{self.kamanda1} vs {self.kamanda2}'

    class Meta:
        verbose_name = 'Keyingi oyın'
        verbose_name_plural = 'Keyingi oyınlar'


class Match(models.Model):
    """Oyın"""
    league = models.CharField(max_length=150, verbose_name="Liga atı")
    kamanda1 = models.CharField(max_length=50, verbose_name="1-kamanda")
    sk1 = models.IntegerField(verbose_name="Kamanda 1 gollar")
    kamanda2 = models.CharField(max_length=50, verbose_name="2-kamanda")
    sk2 = models.IntegerField(verbose_name="Kamanda 2 gollar")
    date = models.DateField(verbose_name='Oqın waqtı (sáne)')
    time = models.CharField(max_length=20, verbose_name='Oqın waqtı (saat)', default='15:00 GMT+5')
    active = models.BooleanField(verbose_name='Aktiv', default=True)

    def __str__(self):
        return f'{self.kamanda1} vs {self.kamanda2}'

    class Meta:
        verbose_name = 'Oyın'
        verbose_name_plural = 'Oyınlar'


class Liga(models.Model):
    """Liga"""
    name = models.CharField(max_length=100, verbose_name='Liga atı')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Liga'
        verbose_name_plural = 'Ligalar'


class LigaStat(models.Model):
    """Liga statistikası"""
    liga = models.ForeignKey(Liga, on_delete=models.CASCADE, related_name='ligateam')
    kamanda = models.CharField(max_length=100, verbose_name='Kamanda')
    match = models.IntegerField(verbose_name='oyın')
    score = models.IntegerField(verbose_name='ochko')

    def __str__(self):
        return f'{self.kamanda} - {self.kamanda}'

    class Meta:
        verbose_name = "Liga kamanda"
        verbose_name_plural = "Liga kamandaları"


class Player(models.Model):
    """Oyınshılar maǵlıwmatı"""
    full_name = models.CharField(max_length=100, verbose_name="Tolıq atı")
    birth_day = models.DateField(default="2023-02-25", verbose_name="Tuwılǵan sáne")
    position = models.CharField(max_length=50, verbose_name="Poziciya")
    image = models.ImageField(upload_to='image/player/')
    desk = models.TextField(verbose_name="Maǵlıwmat", null=True)
    number_player = models.IntegerField(verbose_name="Oyınshı nomeri")
    height = models.FloatField(verbose_name="Oyınshı boyı")
    weight = models.IntegerField(verbose_name="Oyınshı awırlıǵı")

    def __str__(self):
        return f'{self.number_player}. {self.full_name}'

    class Meta:
        verbose_name = "Oyınshı"
        verbose_name_plural = "Oyınshılar"


class Trener(models.Model):
    """Trenerler maǵlıwmatı"""
    full_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='image/player/')
    desk = models.TextField(verbose_name="Maǵlıwmat", null=True)

    def __str__(self):
        return f'{self.full_name}'

    class Meta:
        verbose_name = "Trener"
        verbose_name_plural = "Trenerler"


class Category(models.Model):
    title = models.CharField(max_length=25, verbose_name="Kategoriya")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Kategoriya "
        verbose_name_plural = "Kategoriyalar"

class News(models.Model):
    """Jańalıqlar"""
    title = models.CharField(max_length=250, verbose_name='Qısqa atama')
    summary = models.CharField(max_length=100, verbose_name="Qısqa maqala", null=True)
    body = RichTextUploadingField()
    image = models.ImageField(upload_to='image/news/', verbose_name='Súwret Fon')
    image2 = models.ImageField(upload_to='image/news/', verbose_name='Súwret', null=True)
    date = models.DateField(auto_now_add=True, verbose_name="Sáne")
    caregory = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='cat', null=True)
    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = "Jańalıq"
        verbose_name_plural = "Jańalıqlar"

class Comment(models.Model):
    """Kommentariya - News"""
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='comments')
    full_name = models.CharField(max_length=25, verbose_name="Tolıq atı")
    massage = models.TextField(verbose_name="Xabar")
    created_date = models.DateTimeField(verbose_name="Xabar waqtı", auto_now_add=True)

    def __str__(self):
        return f'{self.news} - {self.full_name}'


class Contact(models.Model):
    """Baylanıs beti"""
    address = models.CharField(max_length=200, verbose_name="Mánzil", default="Adress")
    phone_number = models.CharField(default="+998(90) 123-45-67", verbose_name='Telefon nomeri', max_length=20)
    email = models.EmailField(verbose_name='Elektron pochta')
    image = models.ImageField(upload_to='image/contact/', verbose_name='Súwret Fon')
    location = models.TextField(default="openstreetmap.org", verbose_name="Laylasıw ornı")
    telegram = models.URLField(default="https://t.me/Nurlan_Pirjanov", verbose_name="Telegram kanal", null=True, blank=True)
    instagram = models.URLField(default="https://www.instagram.com/pfkaral_official/", verbose_name="Instagram kanal", null=True, blank=True)


    def __str__(self):
        return f'{self.phone_number} {self.email}'

    class Meta:
        verbose_name = 'Baylanıs'
        verbose_name_plural = 'Baylanıslar'


class Gallery(models.Model):
    """Súwretler"""
    title = models.CharField(max_length=250, verbose_name='Sipatlama')
    image = models.ImageField(verbose_name='Súwret')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Súwret'
        verbose_name_plural = 'Súwretler'