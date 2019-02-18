# Generated by Django 2.1.7 on 2019-02-14 21:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HelpPackage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usable_clothes', models.BooleanField(null=True, verbose_name='Ubrania do ponownego użycia')),
                ('useless_clothes', models.BooleanField(null=True, verbose_name='Ubrania do wyrzucenia')),
                ('toys', models.BooleanField(null=True, verbose_name='Zabawki')),
                ('books', models.BooleanField(null=True, verbose_name='Książki')),
                ('others', models.BooleanField(null=True, verbose_name='Inne')),
                ('bags', models.IntegerField(default=1, verbose_name='Liczba 60l worków')),
                ('street', models.CharField(max_length=64, null=True, verbose_name='Ulica')),
                ('city', models.CharField(max_length=64, null=True, verbose_name='Miasto')),
                ('post_code', models.CharField(max_length=6, null=True, verbose_name='Kod Pocztowy')),
                ('phone_num', models.CharField(max_length=16, null=True, verbose_name='Numer telefonu')),
                ('date', models.DateTimeField(null=True, verbose_name='Data i godzina odbioru')),
                ('comments', models.TextField(null=True, verbose_name='Uwagi dla kuriera')),
            ],
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Nazwa')),
                ('type', models.IntegerField(choices=[(1, 'Fundacja'), (2, 'Organizacja'), (3, 'Lokalna zbiórka')], verbose_name='Rodzaj')),
                ('mission', models.CharField(max_length=255, verbose_name='Misja')),
                ('help', models.IntegerField(choices=[(1, 'dzieciom'), (2, 'samotnym matkom'), (3, 'bezdomnym'), (4, 'niepełnosprawnym'), (5, 'osobom starszym'), (6, 'bezrobotnym')], verbose_name='Komu pomaga')),
                ('date_added', models.DateField(auto_now_add=True, verbose_name='Data dodania')),
            ],
        ),
        migrations.CreateModel(
            name='Towns',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Nazwa')),
                ('province', models.IntegerField(choices=[(1, 'dolnośląskie'), (2, 'lubelskie'), (3, 'łódzkie'), (4, 'mazowieckie'), (5, 'podkarpackie'), (6, 'pomorskie'), (7, 'świętokrzyskie'), (8, 'wielkopolskie'), (9, 'kujawsko-pomorskie'), (10, 'lubuskie'), (11, 'małopolskie'), (12, 'opolskie'), (13, 'podlaskie'), (14, 'śląskie'), (15, 'warmińsko-mazurskie'), (16, 'zachodniopomorskie')], verbose_name='Województwo')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='Data urodzenia')),
                ('description', models.CharField(max_length=255, verbose_name='Opis')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='users/%Y/%m/%d', verbose_name='Zdjęcie profilowe')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Użytkownik')),
            ],
        ),
        migrations.AddField(
            model_name='institution',
            name='town',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='location', to='main.Towns', verbose_name='Miasto'),
        ),
        migrations.AddField(
            model_name='helppackage',
            name='institution',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='organization_name', to='main.Institution', verbose_name='Organizacja'),
        ),
        migrations.AddField(
            model_name='helppackage',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL, verbose_name='Autor'),
        ),
    ]
