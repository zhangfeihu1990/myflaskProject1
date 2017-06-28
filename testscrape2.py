# -*- encoding:UTF-8 -*-
import urllib2
import re
def download(url,user_agent='wswp',numRetries=2):
    print 123
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
    return html
    print 456

def crawl_sitemap(url):
  sitemap = download(url)
  sitemap_regex = re.compile('<loc>(.*?)</loc>')
  #links = re.findall('<loc>(.*?)</loc>',sitemap)
  links = sitemap_regex.findall(sitemap)
  print links
  for link in links:
    print "link: ",links
    #html = download(link)

crawl_sitemap("http://www.ziroom.com/sitemap.xml")

#-----------------------------------------------------
import itertools
for page in itertools.count(1):
    url = '%d' % page
    html = download(url)
    if html is None:
        break
    else:
        pass
#另一个版本
maxi_errors = 5
num_errors = 0
for page in itertools.count(1):
    url = '%d' % page
    html = download(url)
    if html==None:
        num_errors += 1
        if maxi_errors == num_errors:
            break
    else:
        num_errors = 0


#------------------------------------------------
#链接爬虫
#之前已利用网站结构特点实现了两个简单爬虫
#通过跟踪所有链接方式可以很容易下载整个网站页面，但这回下载大量我们不需要的网页，可以用正则表达式确定用哪些页面
import urlparse
def link_crawler(seed_url, link_regex,max_depth=2):
  """
  :param seed_url:
  :param link_regex:
  :return:
  """
  crawl_queue = [seed_url]
  seen = set(crawl_queue)   #避免重复爬取
  while crawl_queue:
      url = crawl_queue.pop()
      html = download(url)
      depth = seen[url]
      if depth != max_depth:
        for link in get_links(html):
          if re.match(link_regex, link):
            link = urlparse.urljoin(seed_url,link)
            if link not in seen:
              seen.add(link)
              seen[link] = depth+1
              crawl_queue.append(link)
def get_links(html):
  webpage_regx = re.compile('<a[^>]+href=["\'](.*? )["\']',re.IGNORECASE)
  return webpage_regx.findall(html)





