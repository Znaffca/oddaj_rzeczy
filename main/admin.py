from django.contrib import admin
from django.utils.safestring import mark_safe

from main.models import UserProfile, Towns, Institution, HelpPackage, HelpType

admin.site.site_header = "Oddaj rzeczy - panel administracyjny aplikacji"
admin.site.site_title = "Oddaj rzeczy"
admin.site.index_title = "Strona główna"


@admin.register(HelpType)
class HelpTypeAdmin(admin.ModelAdmin):
    list_display = 'type',
    fieldsets = ("Komu pomaga", {'fields': ['type']}),


class HelpTypeInline(admin.TabularInline):
    model = Institution.help.through
    extra = 1


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    readonly_fields = ["photo_image"]
    list_display = ['user', 'date_of_birth', 'description', 'photo', 'photo_image']
    list_filter = ('user', 'date_of_birth')
    fieldsets = ('Szczegóły użytkownika', {
            'fields': ('user', 'date_of_birth', 'description', 'photo', 'photo_image')
        }),

    def photo_image(self, obj):
        return mark_safe("<img src='{url}' width='auto' height='50px' >".format(
            url=obj.photo.url,))


@admin.register(Towns)
class TownsAdmin(admin.ModelAdmin):
    list_display = ['name', 'province']
    list_filter = 'province',
    fieldsets = ('Miasto', {'fields': ('name', 'province')}),


@admin.register(Institution)
class InstitutionAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'mission', 'town', 'date_added']
    list_filter = ['type']
    inlines = [HelpTypeInline]
    fieldsets = ('Instytucja', {
        'fields': ('name', 'type', 'mission', 'help', 'town')
    }),


@admin.register(HelpPackage)
class HelpPackageAdmin(admin.ModelAdmin):
    list_display = ['id', 'usable_clothes', 'useless_clothes', 'toys', 'books', 'others', 'bags', 'institution', 'street',
                    'city', 'post_code', 'phone_num', 'date', 'comments', 'user']
    list_filter = ['institution', 'city']
    fieldsets = (
        ('Rzeczy dla potrzebujących', {
            'fields': ('usable_clothes', 'useless_clothes', 'toys', 'books', 'others')
        }),
        ('Liczba 60l worków, w które spakowałeś rzeczy', {
            'fields': ('bags',)
        }),
        ('Wybierz organizację, której chcesz pomóc', {
            'fields': ('institution',)
        }),
        ('Adres odbioru', {
            'fields': ('city', 'street', 'post_code', 'phone_num')
        }),
        ('Termin odbioru', {
            'fields': ('date', 'comments')
        }),
        ('Utworzono przez', {
            'fields': ('user',)
        }),
    )
