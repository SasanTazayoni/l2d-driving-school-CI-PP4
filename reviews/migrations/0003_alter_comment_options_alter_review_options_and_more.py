# Generated by Django 4.2.9 on 2024-01-20 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-replied_on']},
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ['-created_on']},
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='created_on',
            new_name='replied_on',
        ),
    ]