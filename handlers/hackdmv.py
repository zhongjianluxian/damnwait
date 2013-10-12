import webapp2
from google.appengine.api import memcache

class HackDMV(webapp2.RequestHandler):
    def get(self):
        # self.response.write('WOW! CRON job rocks!')
        cnt = memcache.get("cron_key")

        # Increments cnt every time HackDMV is called
        if cnt is None:
        	cnt = 0
        else:
        	cnt = int(cnt) + 1
        	cnt = cnt % 100
        
        memcache.set("cron_key", cnt)
