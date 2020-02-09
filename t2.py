from urllib import parse
import simplejson

#base_url='http://cn.bing.com/search'
url='http://httpbin.org/post'
'''d={
    'q':'马哥教育'
}'''
#https://www.baidu.com/s?wd=%E4%B8%AD
#url='http//www.magedu.com/python?id=1&name=tom'
data=parse.urlencode({'name':'张三,@=/&*','age':'6'})
'''u=parse.urlencode(d)
url='{}?{}'.format(base_url,u)
print(url)
x=parse.unquote(url)
print(x)'''

from urllib.request import urlopen,Request
ua='Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chorme/55.0.2883.75 Safari/537.36'
req=Request(url,headers={
    'User-Agent':ua
})
'''res=Request(url,headers={'User-Agent':ua})'''

print(data)
with urlopen(req,data=data.encode()) as res:
    #with open('f:/bing.html','wb+') as f:
     #   f.write(res.read())
      #  f.flush()
    #print(res.read())
    text=res.read()
    d=simplejson.loads(text)
    print(d)
    print(type(d))
#from urllib.parse import urlencode

'''request=Request('http://httpbin/org/post')
request.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chorme/55.0.2883.75 Safari/537.36')

print(data)
res=urlopen(request,data=data.encode())
with res:
    print(res.read())'''
