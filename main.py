#main.py This is GAE gcloud service
# the import section Imports should always be at the top of the code...

import webapp2

# the handler section
class MainPage(webapp2.RequestHandler):
    def get(self): #for a get request
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello, World!') #the response

class Secretpage(webapp2.RequestHandler):
    def get(self): #get requests
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write('<h1 style="background-color: blue;"> This is my secret page </h1>')

# the app configuration section
app = webapp2.WSGIApplication([
    ('/', MainPage), #this maps the root url to the Main Page Handler
    ('/secret', Secretpage), #this is a secretpage psh
], debug=True)
