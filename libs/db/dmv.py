from google.appengine.ext import ndb

class DMV(ndb.Model):
    dmv_id = ndb.StringProperty(required = True)
    sample_tm = ndb.DateTimeProperty(auto_now_add = True)
    non_appt_wait_mins = ndb.IntegerProperty(required = True)
    appt_wait_mins = ndb.IntegerProperty(required = True)
    weekday = ndb.IntegerProperty()
    
