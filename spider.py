#获取网页链接的方式/网页的GET请求
'''from urllib.request import urlopen,Request

ua="Mozilla/5.0 (Windows NT 6.1;Win64;x64) AppleWebKit/537.36 (KHTML,like Gecko)Chorme/57.0.2987.133 Safari/537.36"
url='http://www.baidu.com/'
res=Request(url,headers={
    'User-agent':'ua'
})
req=urlopen(res)
print(req)
print(type(req))
print(req.geturl())
print(req.read())
print(req.info())
print(req.status)
print(req._method)'''

'''from urllib.request import urlopen,Request
import random

url='https://www.bing.com'

ua_list=[
    "Mozilla/5.0 (Windows NT 6.1;Win64;x64) AppleWebKit/537.36 (KHTML,like Gecko)Chorme/57.0.2987.133 Safari/537.36",
    "Mozilla/5.0 (Windows;U;Windows NT 6.1;zh-CN) AppleWebKit/537.36 (KHTML,like Gecko)Version/5.0.5 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1;Win64;x64;rv:50.0)  Gecko/20100101 Firefox/50.0",
    "Mozilla/5.0 (compatible;MSIE 9.0;Window NT 6.1;tRIDENT/5.0)"
]

ua=random.choice(ua_list)
res=Request(url)
res.add_header('User-agent',random.choice(ua_list))
response=urlopen(res,timeout=20)
print(response.closed)

with response:
    print(type(response))
    print(response.geturl())
    print(response.read())
    print(res.get_header('User-agent'))
print(response.closed)'''


#将获取到的网页链接内容存在本地
'''from urllib import parse
from urllib.request import urlopen,Request

url='https://www.baidu.com/s'
info={
    'name':'python'
}
infor=parse.urlencode(info)
url1='{}?{}'.format(url,parse.urlencode(info))
res=Request(url1,headers={
    'User-agent':"Mozilla/5.0 (Windows NT 6.1;Win64;x64) AppleWebKit/537.36 (KHTML,like Gecko)Chorme/57.0.2987.133 Safari/537.36"
})
with urlopen(res) as r:
    with open('f:/py.html','wb+') as f:
        f.write(r.read())
        f.flush()'''

'''from urllib import parse
from urllib.request import urlopen,Request

base_url='http://cn.bing.com/search'
d={
    'q':'朱镕基'
}
x=parse.urlencode(d)
url='{}?{}'.format(base_url,x)
u=parse.unquote(url)
print(u)

ua='Mozilla/5.0 (Windows;U;Windows NT 6.1;zh-CN) AppleWebKit/537.36 (KHTML,like Gecko)Version/5.0.5 Safari/537.36'
res=Request(url,headers={
    'User-agent':'ua'
})

with urlopen(res) as r:
    with open('f:/zhu.html','wb+') as f:
        f.write(r.read())
        f.flush()'''


#网页的POST请求
'''from urllib.request import urlopen,Request
from urllib import parse
import simplejson

url='http://httpbin.org/post'
data={'name':'易烊千玺','age':19,'gender':'male'}
d=parse.urlencode(data)
print(d)
res=Request(url,headers={
    'User-agent':"Mozilla/5.0 (Windows NT 6.1;Win64;x64) AppleWebKit/537.36 (KHTML,like Gecko)Chorme/57.0.2987.133 Safari/537.36"
})
with urlopen(res,data=d.encode()) as r:
    text=r.read()
    print(text)
    print(type(text))
    t=simplejson.loads(text)
    print('-'*25)
    print(t)
    print(type(t))'''


#获取网页的相对信息
'''from urllib.request import urlopen,Request
from urllib import parse
import simplejson

base_url='https://movie.douban.com/j/search_subjects'
ua="Mozilla/5.0 (Windows NT 6.1;Win64;x64) AppleWebKit/537.36 (KHTML,like Gecko)Chorme/57.0.2987.133 Safari/537.36"
for start in range(0,10):
    d={
        'type':'movie',
        'tag':'热门',
        'page_limit':10,
        'page_start':start
    }
    url='{}?{}'.format(base_url,parse.urlencode(d))
    res=Request(url,headers={
        'User-agent':'ua'
    })
    with urlopen(res) as response:
        rep=simplejson.loads(response.read())
        print(rep)
        print(len(rep['subjects']))'''











