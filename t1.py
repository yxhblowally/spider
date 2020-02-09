from urllib.request import urlopen, Request
import random

from http.client import HTTPResponse

#url='http://ww.bing.com'  #实际上是自由跳转 301 302
url='http://movie.douban.com'

#ua='Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chorme/55.0.2883.75 Safari/537.36'
ua_list=[
    "Mozilla/5.0 (Windows NT 6.1;Win64;x64) AppleWebKit/537.36 (KHTML,like Gecko)Chorme/57.0.2987.133 Safari/537.36",
    "Mozilla/5.0 (Windows;U;Windows NT 6.1;zh-CN) AppleWebKit/537.36 (KHTML,like Gecko)Version/5.0.5 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1;Win64;x64;rv:50.0)  Gecko/20100101 Firefox/50.0",
    "Mozilla/5.0 (compatible;MSIE 9.0;Window NT 6.1;tRIDENT/5.0)"
]
ua=random.choice(ua_list)
req=Request(url)
req.add_header('User-agent',random.choice(ua_list))

response=urlopen(req,timeout=20)   #urlopen可以自动进行跳转
print(response.closed)

with response:
    print(type(response))   #类文件对象
    print(response.status)     #状态
    print(response._method)
    #print(response.read())     #读取返回的内容
    print(response.geturl())     #返回真正的URL
    #print(response.info())     #hearders
    print('-'*30)
   #print(req.method)
    print(req.get_header('User-agent'))

print(response.closed)




