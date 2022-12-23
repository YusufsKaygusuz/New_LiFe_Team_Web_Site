# Generated by Django 4.0.8 on 2022-12-19 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('life', '0018_molecule_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='molecule',
            name='description_de',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='molecule',
            name='description_en',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='molecule',
            name='description_tr',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
    ]