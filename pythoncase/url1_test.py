import urllib.request
import re
n = int(input("请输入："))
n1 = range(1,n+1)
for i in n1:
    qsbk_url = 'https://www.qiushibaike.com/text/page/{}'.format(i)
    user_agent = 'Chrome/4.0 (compatible; MSIE 5.5;Windows NT)'
    req = urllib.request.Request(qsbk_url,headers={'User-Agent':user_agent})
    page = urllib.request.urlopen(req)
    html = page.read().decode('utf-8')
    #print(html)
    r1 = r'<h2>(.*?)</h2>.*?<div class="content">.*?<span>(.*?)</span>.*?<i class="number">(.*?)</i>'
    result = re.findall(r1,html,re.M | re.S)
    print(result)
