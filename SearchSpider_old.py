# -*- coding: cp936 -*-

from baidu import search_baidu
from so import search_so

keyword = raw_input("�����������ؼ��֣�")
filterword = raw_input("������ɸѡ�ؼ��֣�")
filterword = filterword.decode("gbk")

open("baidu.txt", "w").write("����\t����\t�ؼ���\n")
open("360.txt", "w").write("����\t����\t�ؼ���\n")


res_baidu = search_baidu(keyword, filterword)
for r in res_baidu:
    t = "%d\t%s\t%s\n" % (r[0], r[1], keyword)
    open("baidu.txt", "a").write(t)
    
res_so = search_so(keyword.decode("gbk").encode("utf8"), filterword)
for r in res_so:
    t += "%d\t%s\t%s\n" % (r[0], r[1], keyword)
    open("360.txt", "a").write(t)

print
print "���"
print "�����ѱ����� baidu.txt �� 360.txt �ļ���"
raw_input("���س����˳�")
