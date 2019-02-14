from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.conf import settings

PROVINCE_CHOICES = (
    (1, 'dolnośląskie'),
    (2, 'lubelskie'),
    (3, 'łódzkie'),
    (4, 'mazowieckie'),
    (5, 'podkarpackie'),
    (6, 'pomorskie'),
    (7, 'świętokrzyskie'),
    (8, 'wielkopolskie'),
    (9, 'kujawsko-pomorskie'),
    (10, 'lubuskie'),
    (11, 'małopolskie'),
    (12, 'opolskie'),
    (13, 'podlaskie'),
    (14, 'śląskie'),
    (15, 'warmińsko-mazurskie'),
    (16, 'zachodniopomorskie'),
)

ORG_TYPE = (
    (1, "Fundacja"),
    (2, "Organizacja"),
    (3, "Lokalna zbiórka")
)

HELP_CHOICE = (
    (1, "dzieciom"),
    (2, "samotnym matkom"),
    (3, "bezdomnym"),
    (4, "niepełnosprawnym"),
    (5, "osobom starszym"),
    (6, "bezrobotnym"),
)


# extends User class

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Użytkownik")
    date_of_birth = models.DateField(blank=True, null=True, verbose_name="Data urodzenia")
    description = models.CharField(max_length=255, verbose_name="Opis")
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True, null=True, verbose_name="Zdjęcie profilowe")

    def __str__(self):
        return f'{self.user.username}'


# town class

class Towns(models.Model):
    name = models.CharField(max_length=64, verbose_name="Nazwa")
    province = models.IntegerField(choices=PROVINCE_CHOICES, verbose_name="Województwo")

# organization class


class Institution(models.Model):
    name = models.CharField(max_length=128, verbose_name="Nazwa")
    type = models.IntegerField(choices=ORG_TYPE, verbose_name="Rodzaj")
    mission = models.CharField(max_length=255, verbose_name="Misja")
    town = models.ForeignKey(Towns, on_delete=models.CASCADE, related_name="location")
    help = models.IntegerField(choices=HELP_CHOICE, verbose_name="Komu pomaga")
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.type} {self.name}'


# help Package

class HelpPackage(models.Model):
    usable_clothes = models.BooleanField(null=True)
    useless_clothes = models.BooleanField(null=True)
    toys = models.BooleanField(null=True)
    books = models.BooleanField(null=True)
    others = models.BooleanField(null=True)
    bags = models.IntegerField(default=1)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE, related_name="organization_name", null=True)
    street = models.CharField(max_length=64, null=True)
    city = models.CharField(max_length=64, null=True)
    post_code = models.CharField(max_length=6, null=True)
    phone_num = models.CharField(max_length=16, null=True)
    date = models.DateTimeField(null=True)
    comments = models.TextField(null=True)

    def __str__(self):
        return f'{self.institution.name}'
