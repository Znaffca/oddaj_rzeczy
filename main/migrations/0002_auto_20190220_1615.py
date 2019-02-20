# Generated by Django 2.1.7 on 2019-02-20 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HelpType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=128)),
            ],
        ),
        migrations.RemoveField(
            model_name='institution',
            name='help',
        ),
        migrations.AddField(
            model_name='institution',
            name='help',
            field=models.ManyToManyField(to='main.HelpType', verbose_name='Komu pomaga'),
        ),
    ]
