import webapp2

from handlers.mainpage import MainPage
from handlers.testcron import TestCron

app = webapp2.WSGIApplication([('/', MainPage),
                               ('/testcron/?', TestCron)
                               ], debug=True)
