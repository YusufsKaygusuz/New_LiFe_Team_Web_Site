# Generated by Django 4.0.8 on 2022-12-25 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('life', '0024_blog_description_de_blog_description_en_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='short_description',
            field=models.CharField(blank=True, help_text='Gezegenler Hakkında Kısa Bir Deneyim Turu', max_length=255, null=True, verbose_name='Short Description'),
        ),
    ]
