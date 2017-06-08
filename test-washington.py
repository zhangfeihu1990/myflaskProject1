# -*- encoding:UTF-8 -*-
import urllib2
from bs4 import BeautifulSoup
import json
import re
from selenium import webdriver

#下载网页
def download(url, user_agent="wswp"):
  print "开始获取"
  headers = {"User-agent":user_agent}  #设置用户代理
  request = urllib2.Request(url,headers=headers)
  try:
      html = urllib2.urlopen(request).read()
  except urllib2.URLError as e:
      print e
  return html

def crawl_sitemap(url,site):
    html = download(url)
    soup = BeautifulSoup(html,"html.parser")
    print soup.prettify("utf-8")
    if site=="wp":
      print "源自wp"
      storys = soup.find_all(attrs={"moat-id":"homepage/story"})
      print storys
      for story in storys:
        web_headline = story.find(attrs={"data-pb-field":"web_headline"})
        summary = story.find(attrs={"data-pb-field":"summary"})
        if web_headline:
          print "标题：",web_headline.text
        if summary:
          print "简介：",summary.text
    elif site=='cnn':
      #driver = webdriver.Firefox()
      #driver.get("http://edition.cnn.com/")
      #driver.implicitly_wait(30)
     # text = driver.find_element_by_css_selector(".cd__headline-text")
      #print "---------------------" ,text
      print "源自cnn"
      cnn = soup.find_all("script")
      #cnn.stripped_strings
      for i in cnn:            #打印所有js
          data=re.findall(r".*contentModel = (.*)\;\<\/script\>",str(i))
          #data = reg.search(str(i))
          if data:
            #pass
            j = ['{ layout:"no-rail"  , sectionName:"intl_homepage" }']
            j=json.dumps(data)
            print j[0]
            content = json.loads(j)
            print len(content)
            for i in content:
                print content
            #print content[0]
            #print data
      reg = re.compile("\<script\>")#先是要去掉这个头和尾，才会有一个字典的格式，会有key和value
      data = reg.sub(' ',str(cnn))
      print data
      reg3 = re.compile(';\<\/script\>')
      data = reg3.sub('', data)
      print data
      contents = json.loads(data)



      #print cnn.select("CNN.contentModel")

      #contents = soup.find_all(attrs={"data-vr-zone":"home-top-col1"})

      print contents
      print contents
      for content in contents:
          head_line = content.find(attrs={"class":"cd__headline-text"})
          print head_line

class ScrapeCallback:
    def __init__(self):
        pass
    def __call__(self, url, html):
        print url
        print html

crawl_sitemap("http://edition.cnn.com/","cnn")

#print download("http://edition.cnn.com/2017/06/07/politics/james-comey-memos-testimony/index.html")
string = "xxxxxxxxxxxxxxxxxxxxxxxx entry '某某内容' for aaaaaaaaaaaaaaaaaa"

result = re.findall(".*entry(.*)for.*",string)
for x in result:
    print x