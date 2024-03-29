# Generated by Django 4.1.3 on 2024-02-01 07:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, unique=True)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('desc', models.TextField(blank=True)),
                ('poster', models.ImageField(blank=True, upload_to='poster')),
                ('release_date', models.DateTimeField(auto_now_add=True)),
                ('actors', models.TextField(blank=True, max_length=500)),
                ('trailer_link', models.URLField(blank=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finalapp.category')),
            ],
            options={
                'verbose_name': 'movie',
                'verbose_name_plural': 'movies',
                'ordering': ('title',),
            },
        ),
    ]
