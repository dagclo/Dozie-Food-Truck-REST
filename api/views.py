from django.http import HttpResponse, HttpResponseBadRequest
from django.core import serializers

from simple_rest import Resource
import json
import requests

class FoodQuery:
    # This is the sfgov food truck endpoint
    foodTruckUrl = 'https://data.sfgov.org/resource/6a9r-agq8.json'
    
    # This creates the url and adds the query string using the end point
    # I ran into a problem with requests ability to encode the query
    # so I implemented this myself.  I'm using join instead of '+'
    # because it's the most efficient way to concatenate strings
    def createFoodTruckUrl(self, query):
        queryList = [self.foodTruckUrl, '?']
        s = ''
        for queryKey in query.keys():
            queryList.append(queryKey)
            queryList.append('=')
            queryList.append(query[queryKey])
            queryList.append('&')
        queryList.pop()
        return ''.join( queryList )
    
    def milesToMeters(miles):
        return miles * 1609.344
    
    def ProcessFoodItems(self, foodTruckList):
        foodItemDict = {}
        for foodTruck in foodTruckList:
            fooditemlist = foodTruck['fooditems'].split(': ')
            for fooditem in fooditemlist:
                if fooditem in foodItemDict.keys():
                    foodItemDict[fooditem].append(foodTruck['objectid'])
                else:
                    foodItemDict[fooditem] = [foodTruck['objectid']]
        return foodItemDict

class FoodTrucks(Resource, FoodQuery):
    
    def get(self, request, **kwargs):
        query = {'$where': 'within_circle(location,37.78,-122.4, 1000)', 'status' : 'APPROVED', '$limit' : '5', '$offset' : '0'}      
        r = requests.get(self.createFoodTruckUrl(query))
        return HttpResponse(r.json(), content_type='application/json', status=200)
    

class FoodNearMe(Resource, FoodQuery):
    
    # GET REST API
    # Required Parameters: lat and lng for latitude and longitude.  
    # returns bad request if either of those are missing
    # Optional Parameters: meters.  This is set to 1000 if missing.  If less than 0, raises a bad error
    # Returns: Dictionary of fooditems => food truck objectids
    def get(self, request, **kwargs):
        lat = request.GET.get('lat')
        long = request.GET.get('lng')
        meters = request.GET.get('meters')
        if meters == None:
            meters = 1000
        if meters < 0:
           return HttpResponseBadRequest('<h1>meters parameter can not be less than zero</h1>') 
        if lat == None:
            return HttpResponseBadRequest('<h1>Parameter lat is missing</h1>')
        elif long == None:
            return HttpResponseBadRequest('<h1>Parameters lng are missing</h1>')        
        query = {'$where': 'within_circle(location, ' + lat + ', ' + long + ', ' + meters + ')', 'status' : 'APPROVED', '$limit' : '5', '$offset' : '0'}    
        r = requests.get(self.createFoodTruckUrl(query))
        fooditemDict = self.ProcessFoodItems(r.json())
        print fooditemDict
        result = json.dumps(fooditemDict)
        return HttpResponse(result, content_type='application/json', status=200)
        
