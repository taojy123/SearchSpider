# -*- coding: cp936 -*-

import easygui
from baidu import search_baidu
from so import search_so

keywords = easygui.enterbox(u"������ؼ��ʣ�����ؼ����Կո�����").split()
filterword = easygui.enterbox(u"������ɸѡ�ؼ��֣�")

path = easygui.diropenbox(u"��ѡ�����Ŀ¼λ��".encode("utf8")).encode("gbk")

baidufile = path + r"\baidu.txt"
sofile = path + r"\360.txt"

open(baidufile, "w").write("����\t����\t�ؼ���\n")
open(sofile, "w").write("����\t����\t�ؼ���\n")



for keyword in keywords:

    print keyword

    res_baidu = search_baidu(keyword.encode("gbk"), filterword)
    
    for r in res_baidu:
        t = u"%d\t%s\t%s\n" % (r[0], r[1], keyword)
        t = t.encode("gbk")
        open(baidufile, "a").write(t)
        
    res_so = search_so(keyword.encode("utf8"), filterword)
    for r in res_so:
        t = u"%d\t%s\t%s\n" % (r[0], r[1], keyword)
        t = t.encode("gbk")
        open(sofile, "a").write(t)


easygui.msgbox(u"��ɣ������������� " + path.decode("gbk") + u" Ŀ¼��")







