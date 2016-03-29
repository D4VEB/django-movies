from m_ratings.views import top_twenty, movies_page, users_page
from django.conf.urls import url

urlpatterns = [
    url(r'^top_twenty/$', top_twenty, name="top_twenty"),
    url(r'^(?P<id>\d+)/$', movies_page, name="movies_page")
    url(r'^(?P<id>\d+)/$', users_page, name="users_page")
]
