# Generated by Django 4.0.8 on 2023-01-29 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('life', '0031_moleculetest_test_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='moleculetest',
            name='custom_js',
            field=models.TextField(blank=True, null=True),
        ),
    ]
