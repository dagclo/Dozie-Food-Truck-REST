from django.conf.urls import patterns, url, include

from .views import FoodTrucks, FoodNearMe

urlpatterns = patterns('',
    # Allow access to the contacts resource collection
    url(r'^foodtrucks/?$', FoodTrucks.as_view()),
    url(r'^foodnearme/?$', FoodNearMe.as_view()),
)