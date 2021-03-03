# Generated by Django 3.1.2 on 2021-03-03 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actors', '0003_remove_actor_image'),
        ('movies', '0006_movie_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='title',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='movie',
            name='Actors',
            field=models.ManyToManyField(blank=True, null=True, to='actors.Actor'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='Awards',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='BoxOffice',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='Country',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='DVD',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='Director',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='Genre',
            field=models.ManyToManyField(blank=True, null=True, to='movies.Genre'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='Language',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='Metascore',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='Plot',
            field=models.CharField(blank=True, max_length=900, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='Poster',
            field=models.ImageField(blank=True, null=True, upload_to='movies'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='Poster_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='Production',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='Rated',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='Ratings',
            field=models.ManyToManyField(blank=True, null=True, to='movies.Rating'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='Released',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='Runtime',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='Title',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='Type',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='Website',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='Writer',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='Year',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='imdbID',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='imdbRating',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='imdbVotes',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='totalSeasons',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='rating',
            name='rating',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='rating',
            name='source',
            field=models.CharField(max_length=25),
        ),
    ]