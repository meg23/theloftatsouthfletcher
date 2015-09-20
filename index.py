#!/usr/bin/env python

import webapp2
import logging
import json
import os

from google.appengine.api import users
from google.appengine.api import mail
from google.appengine.ext.webapp import template

log = logging.getLogger('webapp')

class Index(webapp2.RequestHandler):

    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.out.write(template.render(path, ""))

    def post(self):
        contact_name = self.request.get('name')
        contact_email = self.request.get('email')
        contact_subject = self.request.get('subject')
        contact_message = self.request.get('message') + "\n Signed %s, %s" % (contact_name, contact_email)

        message = mail.EmailMessage(sender="info@theloft-1034.appspotmail.com",
                            subject=contact_subject)
        message.to = "info@5211southfletcher.com"
        message.body = contact_message
        message.send()

        template_values = {
            'header_title': "Thanks for reaching out %s!" % (contact_name.capitalize()),
            'header_body': "She will get back to you soon, I promise."
        }
        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.out.write(template.render(path, ""))

class Meet(webapp2.RequestHandler):

    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'meet.html')
        self.response.out.write(template.render(path, ""))

app = webapp2.WSGIApplication([('/', Index )], debug=True)


