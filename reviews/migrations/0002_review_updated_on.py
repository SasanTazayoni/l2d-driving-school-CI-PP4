# Generated by Django 4.2.9 on 2024-01-11 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
