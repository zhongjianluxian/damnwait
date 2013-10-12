#add third party libs 
import sys
sys.path.insert(0, 'libs')

import urllib2
import webapp2
from google.appengine.api import memcache
from bs4 import BeautifulSoup
from pytz import timezone
from datetime import datetime

class HackDMV(webapp2.RequestHandler):

    def parseTime(wait_time):
        li = wait_time.split(":")
        return int(li[0])*60 + int(li[1])
    
    def get(self):
        # cnt = memcache.get("cron_key")

        # # Increments cnt every time HackDMV is called
        # if cnt is None:
        # 	cnt = 0
        # else:
        # 	cnt = int(cnt) + 1
        # 	cnt = cnt % 100
        
        # memcache.set("cron_key", cnt)

        #extract wait time information
        id = "548"
        soup = BeautifulSoup(urllib2.urlopen("http://apps.dmv.ca.gov/fo/offices/appl/fo_data_read.jsp?foNumb=%s" %id))
        if "display:block" in soup('div', {'id':'showClosedDiv'})[0]['style']:
            self.response.write('Office closed')
            with open("../cron.yaml") as f:
                for line in f:
                    pass
                last = line
            tz = (last.split(":")[-1]).strip()
            local_timezone = timezone("%s" %tz)
            local_time = local_timezone.localize(datetime.today())
            sys.exit(1)

        else:
            self.response.write("Office is opening")
            appt_wait_time = self.parseTime(soup('span',{'id':'apptWaitTime'})[0].contents[0])
            nonappt_wait_time = self.parseTime(soup('span',{'id':'nonApptWaitTime'})[0].contents[0])
            sys.exit(0)


        