from django.db import models
from autoslug import AutoSlugField

class Geners(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title



class MovieCategory(models.TextChoices):
    COMEDY = 'Comedy', 'Comedy'
    DRAMA = 'Drama', 'Drama'
    ACTION = 'Action', 'Action'
    ROMANCE = 'Romance', 'Romance'
    ADVENTURE = 'Adventure', 'Adventure'




class MovieStatus(models.TextChoices):
    TOP_RATED = 'TR', 'Top Rated'
    TRENDING_NOW = 'TN', 'Trending Now'
    MOST_POPULAR = 'MP', 'Most Popular'


class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000, blank=True)
    image = models.ImageField(upload_to='movies/')
    release_date = models.DateField()
    rating = models.DecimalField(default=0, max_digits=3, decimal_places=1)
    views_count = models.IntegerField(default=0)
    status = models.CharField(choices=MovieStatus.choices, max_length=2)
    category = models.CharField(choices=MovieCategory.choices, max_length=10)
    genres = models.ManyToManyField(Geners)
    new_slug = AutoSlugField(populate_from='title', unique=True, null=True, default=None)
    video = models.FileField(upload_to='videos/', null=True, blank=True)

    def __str__(self):
        return self.title


class Banners(models.Model):
    title = models.CharField(max_length=150)
    cover = models.ImageField(upload_to='banners/')
    category = models.CharField(choices=MovieCategory.choices, max_length=100)

    def __str__(self) -> str:
        return self.title


class Side_items(models.Model):
    title = models.CharField(max_length=150)
    picture = models.ImageField(upload_to='Side-Pics/')
    rating = models.DecimalField(default=0, max_digits=3, decimal_places=1)

    
    def __str__(self) -> str:
        return self.title
