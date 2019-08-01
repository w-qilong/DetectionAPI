import requests
import json
import urllib

# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=Ij64GQf0PKLpWlo9ZENOhujo&client_secret=FBzG2B1bUKCTSCzclxAgDAo9BeefiMOt'
request = urllib.request.Request(host)
request.add_header('Content-Type', 'application/json; charset=UTF-8')
response = urllib.request.urlopen(request)
content = response.read()
if content:
    print(type(content))  # <class 'bytes'>
content_str = str(content, encoding="utf-8")
# eval将字符串转换成字典
content_dir = eval(content_str)
print(content_dir)
access_token = content_dir['access_token']
print(access_token)
