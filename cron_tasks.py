import webapp2

from handlers.hackdmv import HackDMV


app = webapp2.WSGIApplication([('/cron-tasks/hack-dmv', HackDMV),
                               ], debug=True)