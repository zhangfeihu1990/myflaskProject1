# -*- encoding:UTF-8 -*-
import urllib2
import re
from bs4 import BeautifulSoup

def download(url,user_agent='wswp',numRetries=2):
    print 123
    headers = {'User-agent':user_agent}  #设置用户代理
    request = urllib2.Request(url,headers=headers)
    try:
      html =  urllib2.urlopen(request).read()
      print 'hehe'
    except urllib2.URLError as e:
      print "error:", e.reason
      html = None
      if numRetries > 0:
        if hasattr(e,'code') and 500 <= e.code < 600:
            return download(url,user_agent,numRetries-1)
    #print html
    return html
    print 456

def crawl_sitemap(url):
  sitemap = download(url)
  #print sitemap
  soup = BeautifulSoup(sitemap, "html.parser")
  story = soup.find(attrs={"data-feature-id":"homepage/story"})
  summary = story.find(attrs={"data-pb-field":"summary"})
  print summary.text
  #sitemap_regex = re.compile('<loc>(.*?)</loc>')
  #links = re.findall('<loc>(.*?)</loc>',sitemap)
  #links = sitemap_regex.findall(sitemap)
 # sitemap_regx = re.compile('<article*>(.*?)</article>')
  #links = sitemap_regx.findall(sitemap)

  #links = sitemap
  #print links
  #for link in links:
    #print "link: ",links
    #html = download(link)

crawl_sitemap("https://www.washingtonpost.com/")