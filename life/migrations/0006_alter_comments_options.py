# Generated by Django 4.0.8 on 2022-12-10 20:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('life', '0005_comments'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comments',
            options={'verbose_name': 'User Comments', 'verbose_name_plural': 'User Comment'},
        ),
    ]
