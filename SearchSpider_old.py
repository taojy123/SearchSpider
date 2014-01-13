# -*- coding: cp936 -*-

from baidu import search_baidu
from so import search_so

keyword = raw_input("请输入搜索关键字：")
filterword = raw_input("请输入筛选关键字：")
filterword = filterword.decode("gbk")

open("baidu.txt", "w").write("排名\t链接\t关键词\n")
open("360.txt", "w").write("排名\t链接\t关键词\n")


res_baidu = search_baidu(keyword, filterword)
for r in res_baidu:
    t = "%d\t%s\t%s\n" % (r[0], r[1], keyword)
    open("baidu.txt", "a").write(t)
    
res_so = search_so(keyword.decode("gbk").encode("utf8"), filterword)
for r in res_so:
    t += "%d\t%s\t%s\n" % (r[0], r[1], keyword)
    open("360.txt", "a").write(t)

print
print "完成"
print "数据已保存至 baidu.txt 和 360.txt 文件中"
raw_input("按回车键退出")
