from django.conf.urls import patterns, url, include

from .views import FoodTrucks

urlpatterns = patterns('',
    # Allow access to the contacts resource collection
    url(r'^foodtrucks/?$', FoodTrucks.as_view()),
)