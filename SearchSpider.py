# -*- coding: cp936 -*-

from baidu import search_baidu
from so import search_so

keyword = raw_input("请输入搜索关键字：")
filterword = raw_input("请输入筛选关键字：")
filterword = filterword.decode("gbk")

res_baidu = search_baidu(keyword, filterword)
res_so = search_so(keyword.decode("gbk").encode("utf8"), filterword)

s_baidu = "排名\t链接\n"
for r in res_baidu:
    s_baidu += "%d\t%s\n" % (r[0], r[1])
open("baidu.txt", "w").write(s_baidu)
    

s_so = "排名\t链接\n"
for r in res_so:
    s_so += "%d\t%s\n" % (r[0], r[1])
open("360.txt", "w").write(s_so)

print
print "完成"
print "数据已保存至 baidu.txt 和 360.txt 文件中"
raw_input("按回车键退出")
