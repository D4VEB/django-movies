from django.db import models

class Movie(models.Model):

    title = models.CharField(max_length=200)
    genres = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Rater(models.Model):
    gender = models.CharField(max_length=1)
    age = models.SmallIntegerField()
    occupation = models.CharField(max_length=100)
    zip_code = models.SmallIntegerField(max_length=9)

class Genre(models.Model):
    genres = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.genres

class Link(models.Model):
    imdbid = models.SmallIntegerField()
    tmdbid = models.SmallIntegerField()
    movie = models.ForeignKey(Movie)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.imdbid

class Rating(models.Model):
    userid = models.IntegerField()
    rating = models.FloatField()
    movie = models.ForeignKey(Movie)
    rater = models.ForeignKey(Rater)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.rating

class Tag(models.Model):

    userid = models.IntegerField()
    tag = models.CharField(max_length=100)
    movie = models.ForeignKey(Movie)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tag
