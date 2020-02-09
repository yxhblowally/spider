#urllib3
'''import urllib3
from urllib.parse import urlencode
from urllib3.response import HTTPResponse

jurl='https://movie.douban.com/j/search_subjects'
d={
    'type':'movie',
    'tag':'热门',
    'page_limit':10,
    'page_start':10
}

with urllib3.PoolManager()as http:
    response=http.request('GET','{}?{}'.format(jurl,urlencode(d)),headers={
    'User-agent':"Mozilla/5.0 (Windows NT 6.1;Win64;x64) AppleWebKit/537.36 (KHTML,like Gecko)Chorme/57.0.2987.133 Safari/537.36"})
    print(type(response))
   # responsse:HTTPResponse=HTTPResponse
    print(response.status)
    print(response.data)'''


#requests
import urllib3
from urllib.parse import urlencode
from urllib3.response import HTTPResponse
import requests


urls=['https://www.baidu.com/s?wd=magedu','https://www.baidu.com/s?wd=magedu']
session=requests.session()
with session:
    for url in urls:
        response=session.get(url,headers={
            'User-agent':"Mozilla/5.0 (Windows NT 6.1;Win64;x64) AppleWebKit/537.36 (KHTML,like Gecko)Chorme/57.0.2987.133 Safari/537.36"
        })
        with response:
            print(response.text[:50])
            print('-'*30)
            print(response.cookies)
            print('-'*30)
            print(response.request.headers)
            #print(response.url)
            print(response.headers)
            #print(response.encoding)
            #print(response.request)


