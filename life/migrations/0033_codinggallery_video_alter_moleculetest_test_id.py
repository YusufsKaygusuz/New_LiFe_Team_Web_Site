# Generated by Django 4.0.8 on 2023-02-15 17:17

from django.db import migrations, models
import life.models


class Migration(migrations.Migration):

    dependencies = [
        ('life', '0032_moleculetest_custom_js'),
    ]

    operations = [
        migrations.CreateModel(
            name='CodingGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='coding-gallery', verbose_name='Image')),
            ],
            options={
                'verbose_name': 'Kodlama Galerisi',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='video/', verbose_name='Video')),
            ],
            options={
                'verbose_name': 'Videolar',
            },
        ),
        migrations.AlterField(
            model_name='moleculetest',
            name='test_id',
            field=models.CharField(default=life.models.gen_random_string, editable=False, max_length=32, unique=True),
        ),
    ]
