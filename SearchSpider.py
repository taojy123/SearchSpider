# -*- coding: cp936 -*-

from baidu import search_baidu
from so import search_so

keyword = raw_input("�����������ؼ��֣�")
filterword = raw_input("������ɸѡ�ؼ��֣�")
filterword = filterword.decode("gbk")

res_baidu = search_baidu(keyword, filterword)
res_so = search_so(keyword.decode("gbk").encode("utf8"), filterword)

s_baidu = "����\t����\n"
for r in res_baidu:
    s_baidu += "%d\t%s\n" % (r[0], r[1])
open("baidu.txt", "w").write(s_baidu)
    

s_so = "����\t����\n"
for r in res_so:
    s_so += "%d\t%s\n" % (r[0], r[1])
open("360.txt", "w").write(s_so)

print
print "���"
print "�����ѱ����� baidu.txt �� 360.txt �ļ���"
raw_input("���س����˳�")
