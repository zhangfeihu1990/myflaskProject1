import urllib2
def download(url):
    print 123
    content =  urllib2.urlopen(url).read()
    print content
    print 456

download("bj.zu.anjuke.com/")