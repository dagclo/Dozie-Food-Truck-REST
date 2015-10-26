from django.http import HttpResponse
from django.core import serializers

from simple_rest import Resource
import json
from .models import FoodTruck


class FoodTrucks(Resource):

    def get(self, request, **kwargs):
        json_serializer = serializers.get_serializer('json')()
        obj = [ FoodTruck() ]
        contacts = json_serializer.serialize(obj)
        return HttpResponse(contacts, content_type='application/json', status=200)

