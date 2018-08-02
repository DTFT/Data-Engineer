#coding:UTF-8

 

import urllib
import json
from bs4 import BeautifulSoup

tags=[]
url='https://movie.douban.com/j/search_tags?type=movie'
request = urllib.request.Request(url)
response = urllib.request.urlopen(request, timeout=20)
result = json.loads((response.read()).decode('utf-8'))

tags=result['tags']

movies=[]

for tag in tags:
	print(tag)
	limit = 0
	while 1:
		url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=' + tag +'&page_limit=20&page_start=' + str(limit)
		request = urllib.request.Request(url)
		response = urllib.request.urlopen(request, timeout=20)
		result = json.loads((response.read()).decode('utf-8'))

		result=result ['subjects']

		if len(result) == 0:
			break

		for item in result:
			movies.append(item)

	print(len(movies))