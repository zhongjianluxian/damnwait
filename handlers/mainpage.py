#add third party libs 
import sys
sys.path.insert(0, 'libs')

import webapp2
import jinja2
import os
from google.appengine.ext import db
from db import dmv

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)+"/../templates"),
    extensions=['jinja2.ext.autoescape'])

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write('<h1>Welcome to damnwait!</h1>')

        sf = db.GqlQuery("SELECT * from DMV")
        for s in sf.run():
        	self.response.write('<p>%s</p>' % str(s))


        #template = JINJA_ENVIRONMENT.get_template("main.html")
        #self.response.write(template.render())