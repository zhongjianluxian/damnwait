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

    def convertToMinutes(wait_time):
        li = wait_time.split(":")
        return int(li[0])*60 + int(li[1])
    
    def get(self):

        #extract wait time information
        id = "548"
        soup = BeautifulSoup(urllib2.urlopen("http://apps.dmv.ca.gov/fo/offices/appl/fo_data_read.jsp?foNumb=%s" %id))
        if "display:block" in soup('div', {'id':'showClosedDiv'})[0]['style']:
            tz = "America/Los_Angeles"
            local_timezone = timezone("%s" %tz)
            local_time = local_timezone.localize(datetime.today())
            
            memcache.set("sample_local_time", local_time)

        else:
            self.response.write("Office is opening")
            appt_wait_time = self.convertToMinutes(str(soup('span',{'id':'apptWaitTime'})[0].contents[0]))
            nonappt_wait_time = self.convertToMinutes(str(soup('span',{'id':'nonApptWaitTime'})[0].contents[0]))
            
            memcache.set("appt_wait_time", appt_wait_time)
            memcache.set("nonappt_wait_time", nonappt_wait_time)



        