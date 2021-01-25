# Generated by Django 3.1.2 on 2020-11-06 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('actors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=50)),
                ('rating', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=150)),
                ('Year', models.CharField(blank=True, max_length=25)),
                ('Rated', models.CharField(blank=True, max_length=10)),
                ('Released', models.CharField(blank=True, max_length=25)),
                ('Runtime', models.CharField(blank=True, max_length=25)),
                ('Director', models.CharField(blank=True, max_length=100)),
                ('Writer', models.CharField(blank=True, max_length=300)),
                ('Plot', models.CharField(blank=True, max_length=900)),
                ('Language', models.CharField(blank=True, max_length=300)),
                ('Country', models.CharField(blank=True, max_length=150)),
                ('Awards', models.CharField(blank=True, max_length=500)),
                ('Poster', models.ImageField(blank=True, upload_to='movies')),
                ('Poster_url', models.URLField(blank=True)),
                ('Metascore', models.CharField(blank=True, max_length=5)),
                ('imdbRating', models.CharField(blank=True, max_length=5)),
                ('imdbVotes', models.CharField(blank=True, max_length=100)),
                ('imdbID', models.CharField(blank=True, max_length=100)),
                ('Type', models.CharField(blank=True, max_length=10)),
                ('DVD', models.CharField(blank=True, max_length=25)),
                ('BoxOffice', models.CharField(blank=True, max_length=25)),
                ('Production', models.CharField(blank=True, max_length=25)),
                ('Website', models.CharField(blank=True, max_length=150)),
                ('totalSeasons', models.CharField(blank=True, max_length=3)),
                ('Actors', models.ManyToManyField(blank=True, to='actors.Actor')),
                ('Genre', models.ManyToManyField(blank=True, to='movies.Genre')),
                ('Ratings', models.ManyToManyField(blank=True, to='movies.Rating')),
            ],
        ),
    ]
