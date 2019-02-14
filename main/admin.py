from django.contrib import admin
from main.models import UserProfile, Towns, Institution, HelpPackage


admin.site.site_header = "Oddaj rzeczy - panel administracyjny aplikacji"
admin.site.site_title = "Oddaj rzeczy"


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'description', 'photo']
    list_filter = ('user', 'date_of_birth')


@admin.register(Towns)
class TownsAdmin(admin.ModelAdmin):
    list_display = ['name', 'province']
    list_filter = 'province',


@admin.register(Institution)
class InstitutionAdmin(admin.ModelAdmin):
    pass


@admin.register(HelpPackage)
class HelpPackageAdmin(admin.ModelAdmin):
    pass
