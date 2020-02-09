from urllib import parse
from urllib.request import urlopen,Request
import simplejson

ua='Mozilla/5.0 (Windows;U;Windows NT 6.1;zh-CN) AppleWebKit/537.36 (KHTML,like Gecko)Version/5.0.5 Safari/537.36'
jurl='https://movie.douban.com/j/search_subjects'
d={
    'type':'movie',
    'tag':'热门',
    'page_limit':10,
    'page_start':10
}
req=Request('{}?{}'.format(jurl,parse.urlencode(d)),headers={
    'User-agent':'ua'
})

with urlopen(req) as res:
    sub=simplejson.loads(res.read())
    print(len(sub['subjects']))
    print(sub)
