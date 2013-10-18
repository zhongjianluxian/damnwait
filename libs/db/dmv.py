from google.appengine.ext import db

class DMV(db.Model):
    dmv_id = db.StringProperty(required = True)
    sample_tm = db.DateTimeProperty(auto_now_add = True)
    non_appt_wait_mins = db.IntegerProperty(required = True)
    appt_wait_mins = db.IntegerProperty(required = True)
    weekdays = db.IntegerProperty(required = False)
    
