# -*- coding: gbk -*-

import cookielib
import urllib
import time
import re
import traceback
import urllib2
import BeautifulSoup
import pprint
from cookielib import Cookie


cj = cookielib.CookieJar()

opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 5.2) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1'),
                     ('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'), 
                     ('Accept-Language', 'zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3'), 
                     ('Connection', 'keep-alive')
                     ]
opener.addheaders.append( ('Accept-encoding', 'identity') )
opener.addheaders.append( ('Referer', 'http://www.baidu.com/gaoji/preferences.html') )
  

def get_page(url, data=None):
    resp = None
    n = 0
    while n < 5:
        n = n + 1
        try:
            resp = opener.open(url, data)
            page = resp.read()
            return page
        except:
            traceback.print_exc()
            print "Will try after 2 seconds ..."
            time.sleep(2.0)
            continue
        break
    return "Null"


keyword = "我们".decode("gbk").encode("utf8")
filterword = "明星参加".decode("gbk")

def search_so(keyword, filterword):

    url = "http://www.so.com/s?q=" + urllib.quote(keyword)

    res = []
    read = []
    for pnum in range(1,11):
        print "opening page", pnum
        murl = url + "&pn=" + str(pnum)
        mp = get_page(murl)
        mp = mp.decode("utf8", "ignore")
        mp = BeautifulSoup.BeautifulSoup(mp)
        ul = mp.find(id="m-result")
        if not ul:
            continue
        lis = ul.findAll("li", "res-list")

        for i in range(len(lis)):
            item = lis[i]
            sn = (pnum-1)*10 + i + 1
            text = item.getText()
            if filterword in text:
                a = item.find("a")
                if a:
                    href = a.get("href")
                    if href not in read:
                        res.append((sn, href))
                        read.append(href)
                        print href
        
    res.sort()
    pprint.pprint(res)

    return res


if __name__ == "__main__":
    search_so(keyword, filterword)




