# Generated by Django 5.1.1 on 2024-11-20 16:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_note_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='user',
        ),
    ]
