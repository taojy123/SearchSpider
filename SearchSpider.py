# -*- coding: cp936 -*-

import easygui
from baidu import search_baidu
from so import search_so

keywords = easygui.enterbox(u"请输入关键词，多个关键词以空格间隔开").split()
filterword = easygui.enterbox(u"请输入筛选关键字：")

path = easygui.diropenbox(u"请选择输出目录位置".encode("utf8")).encode("gbk")

baidufile = path + r"\baidu.txt"
sofile = path + r"\360.txt"

open(baidufile, "w").write("排名\t链接\t关键词\n")
open(sofile, "w").write("排名\t链接\t关键词\n")



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


easygui.msgbox(u"完成！处理结果保存至 " + path.decode("gbk") + u" 目录中")







