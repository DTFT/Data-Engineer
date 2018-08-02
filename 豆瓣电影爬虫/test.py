

import urllib
import json
from bs4 import BeautifulSoup


# GET
url = 'http://kaoshi.edu.sina.com.cn/college/scorelist?tab=batch&wl=1&local=2&batch=&syear=2'
request = urllib.request.Request(url)
response = urllib.request.urlopen(request, timeout=20)
result = (response.read()).decode('utf-8')

print(result)

'''
# POST
url = 'http://shuju.wdzj.com/depth-data.html'
data = urllib.parse.urlencode({'type1': 1, 'type2': 2, 'status': 0, 'wdzjPlatId': 59})
data = data.encode('utf-8')
new_url = urllib.request.Request(url,data)
response = urllib.request.urlopen(new_url)
result = (response.read()).decode('utf-8')
print(result)
'''