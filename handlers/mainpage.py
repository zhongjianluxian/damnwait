import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Welcome to damnwait!\n\n')
        self.response.write('Enjoy this site! ^_^')