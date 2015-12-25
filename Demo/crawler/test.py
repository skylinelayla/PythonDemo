
from urllib.request import urlopen#导入模块
from bs4 import BeautifulSoup

html = urlopen("http://www.zhihu.com")#调用请求
bsObj=BeautifulSoup(html.read())

print(bsObj.h1)#输出

