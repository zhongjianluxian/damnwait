import webapp2
import jinja2
import os

from utils import render_str

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        # self.response.write('<h1>Welcome to damnwait!</h1>')

        self.response.write(render_str("test.html"))