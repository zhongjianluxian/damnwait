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
        
        G = Line('abcdefghijklmnopqrstsrqponmlkjihgf',encoding='simple')
        G.color('76A4FB')
        G.line(2)
        G.axes('x')
        G.size(600,300)
        G.axes.range(0,10,50,5)

        template_values = {
			"chart_src": str(G)
			}
        self.response.write(render_str("home.html", template_values))