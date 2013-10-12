import webapp2
from google.appengine.api import memcache

class TestCron(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Testing cron tasks...\n')

        cnt = memcache.get("cron_key")

        if cnt is None:
        	self.response.write('Cron task is not running\n')
        else:
        	self.response.write('U have counted to %s' % cnt)


