#!/usr/bin/env python

import urllib2
import urllib

class DynEmail(object):
    def __init__(self, apikey, startdate=None, enddate=None,
            sender=None,debug=False):
        self.apikey = apikey
        self.startdate = startdate
        self.enddate = enddate
        self.sender = sender
        self.debug = debug

    def create_post_data(self):
        """Called thoughout class to create valid post uri"""

        values = { 'apikey' : self.apikey }

        if self.startdate:
            values['startdate'] = self.startdate
        if self.enddate:
            values['enddate'] = self.enddate
        if self.sender:
            values['sender'] = self.sender

        data = urllib.urlencode(values)

        # Debug post data
        if self.debug:
            print data

        return data

    def fetch_request(self,url):
        """Fetch resource"""
        data = self.create_post_data()
        req = urllib2.Request(url, data)
        res = urllib2.urlopen(req)
        return res


    def mailnum(self):
        """
	Get total number of emails sent to gateway
	Returns filetype object in json format
	"""

        url = 'http://emailapi.dynect.net/rest/json/reports/sent/count/'
        res = self.fetch_request(url)
        return res

    def totaldelivered(self):
        """
        note only 500 by default need to send start index from mailnum
        successfully delivered num
        """

        url = 'http://emailapi.dynect.net/rest/json/reports/delivered/count/'
        res = self.fetch_request(url)
        return res.readline()


    def emailsdelivered(self):
        """delivered emailes"""
        url = 'http://emailapi.dynect.net/rest/json/reports/delivered/'
        res = self.fetch_request(url)
        print res.readline()


    def getemails(self):
        """Returns a list of all emails sent through the specified account for
        the specified date range"""
        url = 'http://emailapi.dynect.net/rest/json/reports/sent/'
        res = self.fetch_request(url)
        print res.readline()

    def bounces(self):
        url = 'http://emailapi.dynect.net/rest/json/reports/bounces/count/'
        res = self.fetch_request(url)
        return res

    def bouncemail(self):
        """
	Get bounced mail messages
	@returns dyn file type object in json format
	"""
        url = 'http://emailapi.dynect.net/rest/json/reports/bounces/'
        res = self.fetch_request(url)
        return res

    def complaintnum(self):
	"""Returns Dyn json file type object"""
        url = 'http://emailapi.dynect.net/rest/json/reports/complaints/count'
        res = self.fetch_request(url)
        return res

    def complaintmail(self):
        url = 'http://emailapi.dynect.net/rest/json/reports/complaints/'
        res = self.fetch_request(url)
        print res.readline()

    def issuenum(self):
        url = 'http://emailapi.dynect.net/rest/json/reports/issues/count'
        res = self.fetch_request(url)
        print res.readline()

    def issuemail(self):
        url = 'http://emailapi.dynect.net/rest/json/reports/issues/'
        res = self.fetch_request(url)
        print res.readline()

    def clicks(self):
        url = 'http://emailapi.dynect.net/rest/json/reports/clicks/'
        res = self.fetch_request(url)
        print res.readline()


