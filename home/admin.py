from django.contrib import admin
from .models import *

class MyModelAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'email', 'image')
    def has_add_permission(self, request):
        if Contact.objects.all().count() >= 1:
            return False
        else:
            return True
    # def has_delete_permission(self, request, obj=None):
    #     return False

class LigaInLine(admin.TabularInline):
    model = LigaStat
    extra = 0


class LigaAdmin(admin.ModelAdmin):
    inlines = [LigaInLine]
    list_display = ['name']

class CommentInLine(admin.TabularInline):
    model = Comment
    extra = 0

class CommentAdmin(admin.ModelAdmin):
    inlines = [CommentInLine]


admin.site.register(News, CommentAdmin)
admin.site.register(Liga, LigaAdmin)
admin.site.register(Contact, MyModelAdmin)
admin.site.register(LigaStat)
admin.site.register(Match)
admin.site.register(NextMatch)
admin.site.register(OldMatch)
admin.site.register(Player)
admin.site.register(Trener)
admin.site.register(Gallery)
admin.site.register(LogoFc)