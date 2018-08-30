#coding:utf-8
import re
import urllib.request
n =int(input("请输入页数："))
n1 = range(1,n+1)
count = 0
for i in n1:
    print(i)
    qt_url = 'https://www.qiushibaike.com/pic/page/{}'.format(i)
    user_agent = 'Chrome/4.0 (compatible; MSIE 5.5;Windows NT)'
    req = urllib.request.Request(qt_url,headers={'User-Agent':user_agent})
    page = urllib.request.urlopen(req)
    html = page.read().decode('utf-8')
    r1 = r'<div class="thumb">.*?src="(.*?)" alt'
    re1 = re.findall(r1,html,re.S)
    for u in re1:
        r2 = re.split(r'/medium/(.*?)',u)
        u1 = "https:"+ u
        urllib.request.urlretrieve(u1,"{}".format(r2[2]))
        count += 1
