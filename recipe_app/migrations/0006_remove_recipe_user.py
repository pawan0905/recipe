# Generated by Django 5.1 on 2024-08-28 09:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_app', '0005_alter_recipe_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='user',
        ),
    ]
