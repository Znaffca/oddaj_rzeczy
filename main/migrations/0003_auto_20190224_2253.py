# Generated by Django 2.1.7 on 2019-02-24 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_helppackage_date_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='helppackage',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
