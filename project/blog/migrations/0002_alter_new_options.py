# Generated by Django 4.1 on 2022-08-07 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='new',
            options={'verbose_name': 'Пост', 'verbose_name_plural': 'Новости'},
        ),
    ]
