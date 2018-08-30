import urllib.request
qsbkurl = 'https://www.qiushibaike.com/'
user_agent = 'Chrome/4.0 (compatible; MSIE 5.5;Windows NT)'
req = urllib.request.Request(qsbkurl,headers={'User-Agent':user_agent})
page = urllib.request.urlopen(req)
html = page.read().decode('utf-8')
print(html)
#urllib.request.urlretrieve('https://pic.qiushibaike.com/system/pictures/12085/120850426/medium/KSUR07PLGM57EMWY.jpg')
