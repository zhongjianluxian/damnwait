#add third party libs 
import sys
sys.path.insert(0, 'libs')

import webapp2
import jinja2
import os

from GChartWrapper import *
from utils import render_str
from db import dmv
from google.appengine.ext import ndb
from google.appengine.ext.ndb import Query

class MainPage(webapp2.RequestHandler):
    
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        
        template_values = {
			"chart_src": ""
			}
        self.response.write(render_str("home.html", template_values))

class WaitTimeQuery(webapp2.RequestHandler):
    
    def post(self):
        self.response.headers['Content-Type'] = 'text/html'
        office = self.request.get("office")
        weekday = self.request.get("weekday")
        
        q = dmv.DMV.query().filter(ndb.GenericProperty('dmv_id') == office).filter(ndb.GenericProperty('weekday') == int(weekday))
        
        a= q.fetch()



        self.response.write(a)
        
