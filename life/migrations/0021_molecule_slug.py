# Generated by Django 4.0.8 on 2022-12-25 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('life', '0020_molecule_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='molecule',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True, verbose_name='Slug'),
        ),
    ]
