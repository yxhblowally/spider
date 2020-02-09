from urllib.request import urlopen,Request


res=Request('https://www.12306.cn/mormhweb/')
res.add_header(
    'User-agent',"Mozilla/5.0 (Windows NT 6.1;Win64;x64) AppleWebKit/537.36 (KHTML,like Gecko)Chorme/57.0.2987.133 Safari/537.36"
)
with urlopen(res) as r:
    print(r._method)
    print(r.read())