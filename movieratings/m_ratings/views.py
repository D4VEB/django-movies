from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.template import loader, Context

from m_ratings.models import Movie

def top_twenty(request):
    """
    The top 20 movies rated. This list of movies should have their
    average rating, and each movie listed should have a link to
    its individual page
    """

def movies_page(request):
    """
    Each individual movie. This page should have the movie, its average
    rating, and each person who rated it. The list of people should have
    the rating with each person and should have a link to that person's page.
    """
    movie = get_object_or_404(Movie, pk=id)
    time_run = timezone.now()
    return render(request, "movies/movies_page.html",
                  {"movie": movie, "time_run": time_run})

def users_page(request):
    """
    Each individual user. This page should have their demographic data,
     and a list of all movies they've rated, with the rating they gave it.
     Each movie listed should have the rating they gave it beside it and
     should have a link to that movie's page
    """
