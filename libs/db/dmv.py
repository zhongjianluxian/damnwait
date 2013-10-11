from google.appengine.ext import db

class DMV(db.Model):
	name = db.StringProperty(required = True)
	mnemonic = db.StringProperty(required = True)
	address = db.PostalAddressProperty(required = True)
	telephone = db.PhoneNumberProperty(required = True)
	email = db.EmailProperty()
	sample_tm = db.DateTimeProperty()
	wait_time_non_appt = db.FloatProperty()
	wait_time_appt = db.FloatProperty()
	updt_tm = db.DateTimeProperty(auto_now_add = True)
	