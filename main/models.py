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


# help type class

class HelpType(models.Model):
    type = models.CharField(max_length=128)

    def __str__(self):
        return self.type

    class Meta:
        verbose_name_plural = "Typy pomocy"


# extends User class

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Użytkownik")
    date_of_birth = models.DateField(blank=True, null=True, verbose_name="Data urodzenia")
    description = models.CharField(max_length=255, verbose_name="Opis")
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True, null=True, verbose_name="Zdjęcie profilowe")
    phone_num = models.CharField(max_length=20, verbose_name="Telefon")

    def __str__(self):
        return f'{self.user}'

    class Meta:
        verbose_name_plural = "Profile użytkowników"


# town class

class Towns(models.Model):
    name = models.CharField(max_length=64, verbose_name="Nazwa")
    province = models.IntegerField(choices=PROVINCE_CHOICES, verbose_name="Województwo")

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = "Miasta"

# organization class


class Institution(models.Model):
    name = models.CharField(max_length=128, verbose_name="Nazwa")
    type = models.IntegerField(choices=ORG_TYPE, verbose_name="Rodzaj")
    mission = models.CharField(max_length=255, verbose_name="Misja")
    town = models.ForeignKey(Towns, on_delete=models.CASCADE, related_name="location", verbose_name="Miasto")
    help = models.ManyToManyField(HelpType, verbose_name="Komu pomaga", related_name='helptype')
    date_added = models.DateField(auto_now_add=True, verbose_name="Data dodania")

    def __str__(self):
        return f'{self.type} {self.name}'

    class Meta:
        verbose_name_plural = "Zaufane instytucje"


# help Package

class HelpPackage(models.Model):
    usable_clothes = models.BooleanField(default=False, verbose_name="Ubrania do ponownego użycia")
    useless_clothes = models.BooleanField(default=False, verbose_name="Ubrania do wyrzucenia")
    toys = models.BooleanField(default=False, verbose_name="Zabawki")
    books = models.BooleanField(default=False, verbose_name="Książki")
    others = models.BooleanField(default=False, verbose_name="Inne")
    bags = models.IntegerField(default=1, verbose_name="Liczba 60l worków")
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE, related_name="organization_name", null=True,
                                    verbose_name="Organizacja")
    street = models.CharField(max_length=64, null=True, verbose_name="Ulica")
    city = models.CharField(max_length=64, null=True, verbose_name="Miasto")
    post_code = models.CharField(max_length=6, null=True, verbose_name="Kod Pocztowy")
    phone_num = models.CharField(max_length=16, null=True, verbose_name="Numer telefonu")
    date = models.DateField(null=True, verbose_name="Data odbioru")
    time = models.TimeField(null=True, verbose_name="Godzina odbioru")
    comments = models.TextField(null=True, verbose_name="Uwagi dla kuriera")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user",
                             verbose_name="Autor")
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        pass

    class Meta:
        verbose_name_plural = "Utworzone dary"


# Delivered informations

class DeliveredPackage(models.Model):
    package = models.ForeignKey(HelpPackage, on_delete=models.CASCADE, verbose_name="Dar")
    delivered = models.BooleanField(default=False, verbose_name="Dostarczono do fundacji")
    date_delivered = models.DateTimeField(auto_now_add=True, verbose_name="Data dostarczenia")

    def __str__(self):
        return f'{self.date_delivered}'

    class Meta:
        verbose_name_plural = "Informacje o dostarczeniu do fundacji"
