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

"""
cj._cookies = {'.baidu.com': {'/': {'BAIDUID': Cookie(version=0, name='BAIDUID', value='BEDAD77137C248AB73FDD54B0641FB96:SL=0:NR=100:FG=1',
                                                      port=None, port_specified=False, domain='.baidu.com', domain_specified=True, domain_initial_dot=True, path='/',
                                                      path_specified=True, secure=False, expires=1420788563, discard=False, comment=None, comment_url=None, rest={},
                                                      rfc2109=True)}}}
"""         

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


keyword = "abc"
filterword = "abcnews".decode("gbk")

def search_baidu(keyword, filterword):

    url = "http://www.baidu.com/s?rn=100&wd=" + urllib.quote(keyword)
    mp = get_page(url)
    mp = BeautifulSoup.BeautifulSoup(mp)

    tabs = mp.findAll("table", "result")
    divs = mp.findAll("div", "result-op")

    links = []
    for item in tabs + divs:
        sn = item.get("id")
        text = item.getText()
        if filterword in text:
            a = item.find("a")
            if a:
                href = a.get("href")
                links.append((href, sn))
                
    pprint.pprint(links)

    res = []
    for link in links:
        try:
            tp = urllib2.urlopen(link[0], timeout=60)
            url = tp.url
            sn = link[1]
            res.append((int(sn), str(url)))
            print url
        except:
            print "can't open", link[0]
            #open("error.txt", "a").write(link[0] + "\n")
        
    res.sort()
    pprint.pprint(res)

    return res






