#add third party libs 
import sys
sys.path.insert(0, 'libs')

import webapp2
import jinja2
import os

from GChartWrapper import *
from utils import render_str

class MainPage(webapp2.RequestHandler):
    
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        
        G = Line('abcdefghijklmnopqrstsrqponmlkjihgfdasdsadhaskldhaskldhsakjldhdhakjhdwhwjhkjawhdjkahdjk',encoding='simple')
        G.color('76A4FB')
        G.line(4)
        G.size(600, 300)
        G.axes('xy')
        G.axes.range(0,8,17,1)
        G.axes.range(1,0,200,50)
        G.axes.label(0, '8AM', '9', '10', '11', '12PM', '1', '2', '3', '4', '5PM')
        G.marker('fMax','red',0,19,10)
        G.grid(8,17,1,0)

        template_values = {
			"chart_src": str(G)
			}
        self.response.write(render_str("home.html", template_values))

class WaitTimeQuery(webapp2.RequestHandler):
    
    def post(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write("<h1>this is a test</h1>")