# Generated by Django 4.2.9 on 2024-02-15 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_alter_userprofile_about_me'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='about_me',
            field=models.TextField(blank=True, max_length=400, null=True),
        ),
    ]