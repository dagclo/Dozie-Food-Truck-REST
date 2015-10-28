from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
import requests

# Create your views here.

def index(request):
    template = loader.get_template('showcase/index.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))

