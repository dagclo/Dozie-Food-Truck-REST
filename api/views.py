from django.http import HttpResponse
from django.core import serializers

from simple_rest import Resource
import json
from .models import FoodTruck
import requests


class FoodTrucks(Resource):
    foodTruckUrl = 'https://data.sfgov.org/resource/6a9r-agq8.json'
    def get(self, request, **kwargs):
        query = {'$where': 'within_circle(location,37.78,-122.4, 1000)', 'status' : 'APPROVED', '$limit' : '5', '$offset' : '0'}      
        r = requests.get(self.createFoodTruckQuery(query))
        return HttpResponse(r.json(), content_type='application/json', status=200)
    
    def createFoodTruckQuery(self, query):
        queryList = [self.foodTruckUrl, '?']
        s = ''
        for queryKey in query.keys():
            queryList.append(queryKey)
            queryList.append('=')
            queryList.append(query[queryKey])
            queryList.append('&')
        queryList.pop()
        return ''.join( queryList )