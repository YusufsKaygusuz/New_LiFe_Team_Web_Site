# Generated by Django 4.0.8 on 2022-12-10 14:14

from django.db import migrations, models
import life.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewLifeManagementMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Title ( ex: Software Engineer )', max_length=255, verbose_name='Title')),
                ('full_name', models.CharField(help_text='Full Name ( ex: Elon Musk )', max_length=255, verbose_name='Full Name')),
                ('linkedin', models.URLField(help_text='Linkedin link', verbose_name='Linkedin URL')),
                ('instagram', models.URLField(help_text='Instagram link', verbose_name='Instagram URL')),
                ('position', models.PositiveSmallIntegerField(unique=True, verbose_name='Ordering Number')),
                ('image', models.ImageField(upload_to=life.models.management_member_image_path, verbose_name='Member Image')),
            ],
            options={
                'verbose_name': 'Management Members',
                'verbose_name_plural': 'Management Member',
                'ordering': ('position',),
            },
        ),
    ]
