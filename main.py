import os
from google.appengine.ext.webapp import template

home_tmpl = os.path.join(os.path.dirname(__file__), 'markup/home.html')

print 'Content-Type: text/html'           # let the browser know that it's getting html
print ''
print template.render(home_tmpl, {})      # return response content - the text itself


