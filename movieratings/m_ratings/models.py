from django.db import models

    # Create Django models to represent the data.
    # Make sure that the data has the appropriate data
    # types. For simplicity sake you may skip the
    # genre_movies table and skip the many to many
    # relationship between movie and genre.

class Movie(models.Model):

    # movieid = models.SmallIntegerField()
    title = models.CharField(max_length=200)
    genres = models.CharField(max_length=200)
    # mpaa_rating = models.CharField(default = null)


    # Make sure each model has 2 additional fields
    # to track the date added and the date modified.

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Genre(models.Model):
    genres = models.CharField(max_length=200)
    # id = models.SmallIntegerField()
        # NOTE FROM CLASS HW Review. For a many-to-many...
        # movies = models.ManyToManyField(Movie)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.genres

class Link(models.Model):
    # movieid = models.SmallIntegerField()
    imdbid = models.SmallIntegerField()
    tmdbid = models.SmallIntegerField()

    movie = models.ForeignKey(Movie)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.imdbid

class Rating(models.Model):
    userid = models.IntegerField()
    # movieid = models.SmallIntegerField()
    rating = models.FloatField()
    # timestamp = models.?
    # id = models.SmallIntegerField()

    movie = models.ForeignKey(Movie)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.rating

class Tag(models.Model):

    userid = models.IntegerField()
    # movieid = models.SmallIntegerField()
    tag = models.CharField(max_length=100)
    # timestamp = models.?
    # id = models.SmallIntegerField()

    movie = models.ForeignKey(Movie)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tag
