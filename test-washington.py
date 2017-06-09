# -*- encoding:UTF-8 -*-
import urllib2
from bs4 import BeautifulSoup
import json
import re
import time
import simplejson
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

def download2(url, user_agent="wswp"):
  print "开始获取"
  headers = {"User-agent":user_agent}  #设置用户代理
  request = urllib2.Request(url,headers=headers)
  try:
      re = urllib2.urlopen(request)
      time.sleep(20)
      html = re.read()
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
      #cnn = soup.find_all(attrs={"class":"cd__headline-text"})
      print cnn
      #cnn.stripped_strings
      for i in cnn:            #打印所有js
          print "i type:",type(i)
          data=re.findall(r".*contentModel = (.*)\;\<\/script\>",str(i))

          #data = reg.search(str(i))
          if data:
            print "类型：" ,type(data)
            print len(data)
            print  re.sub(r'\s+', ' ', data[0])    #去除掉多余空格
            dd = re.sub(r'\s+', ' ', data[0])

            print "list内容：",'='.join(data[0].split(':'))
            print "-------listtype:",type(data[0])

            #pass
            #j = ['{ layout:"no-rail"  , sectionName:"intl_homepage" }']
            data= simplejson.dumps(dd)
            print "-------data type:" ,type(data)
            ddd = dict({"a":1,"b":2})
            #dict_data1 = dict(':'.join(data[0].split(':')))
            #dict_data = dict(eval(data))
           # print "dict_data type:",type(dict_data)
            #print j[1]
            content = simplejson.loads(data,encoding='utf-8')
            print content
            a = content.split(',')
            print "个数%d",len(a)
            uri_list=[]    #盛装需要内容的字典
            contentList = ["publishDate","pageBranding"]
            for k in range(0,len(a)):
                print a[k]
                b = a[k].split(":")

                for m in range(0,len(b)):
                  print "key,val",b[m]
                if '{"uri"' in str(b[0]):
                #if str(b[0]) in contentList:
                    uri_list.append(b[1])
                #if 'pageBranding' in str(b[0]):
                    #mydic[b[0]] = b[1]
            print "mydic:",uri_list
            url_list = []
            for j in range(0,len(uri_list)):
                print "http://edition.cnn.com/"+str(uri_list[j]).strip('"')  #去除uri两侧双引号，构成完整url
                url = "http://edition.cnn.com/"+str(uri_list[j]).strip('"')
                if url.endswith("html"):
                  url_list.append(url)

            print len(uri_list),len(url_list),url_list
            print "a:",type(a),a

            #content = json.loads(data)
            print "-------content type:" ,type(content)
            #dict(content.encode("utf-8"))
            #content = eval(content.encode("utf-8"))

            #for i in content:
               # print content
            #print content[0]
            #print data
      reg = re.compile("\<script\>")#先是要去掉这个头和尾，才会有一个字典的格式，会有key和value




      #print cnn.select("CNN.contentModel")

      #contents = soup.find_all(attrs={"data-vr-zone":"home-top-col1"})



class ScrapeCallback:
    def __init__(self):
        pass
    def __call__(self, url, html):
        print url
        print html

crawl_sitemap("http://edition.cnn.com/","cnn")
def crow_cnn():
    html = download("http://edition.cnn.com/2017/06/08/europe/jeremy-corbyn-election-gains-shock/index.html")
    soup = BeautifulSoup(html,"html.parser")
   # print soup.prettify("utf-8")
    print soup.find(attrs={"class":"update-time"}).text
    contents = soup.find_all(attrs={"class":"zn-body__paragraph"})
    for i in contents:
      print i.text
#crow_cnn()


