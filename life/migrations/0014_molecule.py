# Generated by Django 4.0.8 on 2022-12-12 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('life', '0013_alter_comment_rate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Molecule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Molecule name', max_length=255, verbose_name='Molecule Title')),
                ('title_tr', models.CharField(help_text='Molecule name', max_length=255, null=True, verbose_name='Molecule Title')),
                ('title_en', models.CharField(help_text='Molecule name', max_length=255, null=True, verbose_name='Molecule Title')),
                ('title_de', models.CharField(help_text='Molecule name', max_length=255, null=True, verbose_name='Molecule Title')),
                ('embed_link', models.URLField(help_text='ex: https://embed.molview.org/v1/?mode=balls&cid=1049', verbose_name='Embed Link')),
            ],
            options={
                'verbose_name': 'Molecule',
                'verbose_name_plural': 'Molecules',
            },
        ),
    ]
