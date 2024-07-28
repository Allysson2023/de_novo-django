from django.contrib import admin
from django.http import HttpRequest
from site_setup.models import MenuLink, SiteSetup

# Register your models here.

# esse foi um menu link no banco de dados que ja ta no siteSetup
# @admin.register(MenuLink)
# class MenuLinkAdmin(admin.ModelAdmin):

#     list_display = 'id','text', 'url_or_path',
#     list_display_links = 'id','text', 'url_or_path',
#     search_fields = 'id','text', 'url_or_path',


class MenuLinkInline(admin.TabularInline):
    model = MenuLink
    extra = 1


@admin.register(SiteSetup)
class SiteSetupAdmin(admin.ModelAdmin):

    list_display = 'title','description',
    inlines = MenuLinkInline,


#esse metodo e quando a pessoa bota so uma publicaçao, ser tem ou nao somente uma vez....ser quizer que a pessoa bota a mais so tira oque tem em baixo..
    def has_add_permission(self, request):
        return not SiteSetup.objects.exists()
    