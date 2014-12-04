# -*- coding: utf-8 -*-

# This class will return an list of links on the
# the web page provided

import urllib2
from bs4 import BeautifulSoup


class UrlLinks(object):

    def __init__(self, url):
        self.url = url
        self.links = set()

    def getLinks(self):
        try:
            response = urllib2.urlopen(self.url).read()
            soup = BeautifulSoup(response)
            for line in soup.find_all('a'):
                url = line.get('href')
                if url is not None and url.startswith("http"):
                    self.links.add(url)
        except urllib2.HTTPError as e:
            print e.reason

        return self.links

'''
w = UrlLinks('http://www.example.com')
for i in w.getLinks():
    print(i)
'''