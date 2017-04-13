# -*- encoding:UTF-8 -*-
import urllib2
import re
import csv
from bs4 import BeautifulSoup
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
    print html
    #regx = re.compile('<p class="price">(.*?)</p>')
    #allprice = regx.findall(html)
    soup = BeautifulSoup(html,"html.parser")
    allprice = soup.find_all('p',attrs={"class":"price"})
    for price in allprice:
        #print price.text.split('\t')
        regx = re.compile(r'[0-9]')
        price = regx.findall(str(price))
        print price

    if scrape_callback:
      links.extend(scrape_callback(html) or [])
    print 456


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


download("http://www.ziroom.com/z/nl/s4%E5%8F%B7%E7%BA%BF-t%E9%BB%84%E6%9D%91%E8%A5%BF%E5%A4%A7%E8%A1%97-z3.html"
         ,scrape_callback=ScrapeCallback())