# -*- encoding:UTF-8 -*-
import urllib2
import re
import csv
from bs4 import BeautifulSoup
import json
import string
def download(url,user_agent='wswp',numRetries=2,scrape_callback=None):
    print 123
    links=[]
    headers = {'User-agent':user_agent}  #设置用户代理
    request = urllib2.Request(url,headers=headers)
    try:
      html =  urllib2.urlopen(request).read()
    except urllib2.URLError as e:
      print "error:", e.reason
      html = None
      if numRetries > 0:
        if hasattr(e,'code') and 500 <= e.code < 600:
            return download(url,user_agent,numRetries-1)
    #print html
    print json.loads(html)

    # if scrape_callback:
    #   links.extend(scrape_callback(html) or [])
    print 456
    return html


class ScrapeCallback:
    def __init__(self):
        self.writer = csv.writer(open('f:/houses.csv','w'))
        #self.csv = open('f:/houses.csv','w')
        self.fields = ('price')
        self.writer.writerow(self.fields)
        #self.csv.write(self.fields)
    def __call__(self,html):
      soup = BeautifulSoup(html,"html.parser")
      allprice = soup.find_all('p',attrs={"class":"price"})
      row = []
      for price in allprice:

        price1 = price.text.decode("utf-8")
        #self.csv.write(price)
        row.append(price)
        self.writer.writerow(row)


# download("http://example.webscraping.com/ajax/search.json?&search_term=a&page_size=4&page=0"
#          ,scrape_callback=ScrapeCallback())

def scrape_ajax():
    #template_url = 'http://example.webscraping.com/ajax/search.json?search_term=%(term)s&page=%(page)s&page_size=10'
    template_url = 'http://example.webscraping.com/ajax/search.json?search_term={}&page={}&page_size=10'
    countries = set()
    for letter in string.lowercase:
        page = 0
        while True:
          template_url=template_url.format(letter,page)
          #data={'term':letter,'page':page}
          #template_url=template_url % data
          html = download(template_url,scrape_callback=ScrapeCallback())
          ajax = json.loads(html)
          for record in ajax['records']:
              countries.add(record['country'])
          page+=1
          print "page:", page
          if ajax is None or page>3:
              break

scrape_ajax()


