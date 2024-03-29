# Generated by Django 4.1.3 on 2024-02-08 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addapp', '0002_movie'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('desc', models.TextField(blank=True)),
                ('img', models.ImageField(blank=True, upload_to='genre')),
            ],
        ),
    ]
