# Generated by Django 4.1.3 on 2024-02-08 08:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('addapp', '0004_alter_category_options'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Movie',
        ),
    ]