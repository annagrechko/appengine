import cgi
import webapp2

class MainPage(webapp2.RequestHandler):

    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello, World!')

class GoodbyePage(webapp2.RequestHandler):

    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Goodbye, World.  Time to sleep.')

app = webapp2.WSGIApplication([
     ('/', MainPage),
    ('/goodbye', GoodbyePage),
], debug=True)