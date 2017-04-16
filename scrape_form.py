# -*- encoding:UTF-8 -*-
import urllib, urllib2
from bs4 import BeautifulSoup
import pprint
import cookielib

'''
获取页面中所有input元素的name：value 键值对
'''
def parse_form(html):
  data = {}
  soup = BeautifulSoup(html,"html.parser")
  allElement = soup.find_all('input')#,attrs={"class":"price"}
  for element in allElement:
    if element.get('name'):
      #print element.get('name')
      data[element.get('name')] = element.get('value')
  #print data
  pprint.pprint(data)
  return data

LOGIN_URL = 'https://passport.csdn.net/'
LOGIN_EMAIL = '963076844@qq.com'
LOGIN_PASSWORD = 'zfh1990AAA'
# data = {'username':LOGIN_EMAIL,'password':LOGIN_PASSWORD}
# data['lt'] = 'LT-385052-NBqOWgjxoXkyuHfbeObfaVz3cFXyG5'
# data['execution'] = 'e3s1'
# data['_eventId'] = 'submit'
# data['rememberMe'] = 'true'

# headers = {'User-agent':'wswp'}  #设置用户代理
# request = urllib2.Request('https://passport.csdn.net/account/login?ref=toolbar',headers=headers)
# html =  urllib2.urlopen(request).read()
# data = parse_form(html)

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
html = opener.open(LOGIN_URL).read()
data = parse_form(html)
data['username'] = LOGIN_EMAIL
data['password'] = LOGIN_PASSWORD


encoded_data = urllib.urlencode(data)
request = urllib2.Request(LOGIN_URL,encoded_data)
response = urllib2.urlopen(request)
print response.geturl()