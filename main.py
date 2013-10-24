import webapp2

from handlers.mainpage import MainPage
from handlers.testcron import TestCron
from handlers.mainpage import WaitTimeQuery

app = webapp2.WSGIApplication([('/', MainPage),
                               ('/testcron/?', TestCron),
                               ('/submit/?', WaitTimeQuery)
                               ], debug=True)
