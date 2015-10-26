import re

from piston.handler import BaseHandler
from piston.utils import rc, throttle

class FoodTruckHandler(BaseHandler):
    allowed_methods = ('GET',)
   
    def read(self, request): 
        resp = rc.ALL_OK
        resp.write("cat dog man")
        return resp