# Generated by Django 4.0.8 on 2022-12-10 20:19

from django.db import migrations, models
import life.models


class Migration(migrations.Migration):

    dependencies = [
        ('life', '0004_alter_newlifemanagementmember_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_full_name', models.CharField(help_text='ex: Berkay Şen', max_length=255, verbose_name='User Full Name')),
                ('user_image', models.ImageField(blank=True, upload_to=life.models.comment_user_image_path, verbose_name='User Image')),
                ('rate', models.PositiveSmallIntegerField(choices=[('1', '1 Star'), ('1.5', '1.5 Star'), ('2', '2 Star'), ('2.5', '2.5 Star'), ('3', '3 Star'), ('3.5', '3.5 Star'), ('4', '4 Star'), ('4.5', '4.5 Star'), ('5', '5 Star')], help_text='ex: 4', verbose_name='Comment Star')),
                ('comment', models.TextField(help_text='ex: Very nice..', verbose_name='User Comment')),
            ],
        ),
    ]