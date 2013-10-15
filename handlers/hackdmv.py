#add third party libs 
import sys
sys.path.insert(0, 'libs')

import urllib2
import webapp2
from google.appengine.api import memcache
from bs4 import BeautifulSoup
from pytz import timezone
from datetime import datetime
from db import dmv
import json
import os

class HackDMV(webapp2.RequestHandler):

    def convertToMinutes(self, wait_time):
        li = wait_time.split(":")
        return int(li[0])*60 + int(li[1])
    
    def get(self):

        #read the dmv_info file
        f = open(os.path.dirname(__file__)+"/../dmv_info.json")
        dmv_list = json.load(f)
        id_list = [ int(dmv['dmv_id']) for dmv in dmv_list ]

        #extract wait time information
        for id in id_list:
            soup = BeautifulSoup(urllib2.urlopen("http://apps.dmv.ca.gov/fo/offices/appl/fo_data_read.jsp?foNumb=%s" %id))
            if "display:block" in soup('div', {'id':'showClosedDiv'})[0]['style']:
                tz = "America/Los_Angeles"
                local_timezone = timezone("%s" %tz)
                local_time = local_timezone.localize(datetime.today())
                
                memcache.set("sample_local_time", local_time)

            else:
                appt_wait_time = self.convertToMinutes(str(soup('span',{'id':'apptWaitTime'})[0].contents[0]))
                nonappt_wait_time = self.convertToMinutes(str(soup('span',{'id':'nonApptWaitTime'})[0].contents[0]))
                
                #insert data into data store
                t = dmv.DMV( dmv_id = id,
                    sample_tm = datetime.now(),
                    non_appt_wait_mins = nonappt_wait_time,
                    appt_wait_mins = appt_wait_time
                    )
                
                t.put()

                #for cron job testing purpose
                memcache.set("appt_wait_time", appt_wait_time)
                memcache.set("nonappt_wait_time", nonappt_wait_time)



        