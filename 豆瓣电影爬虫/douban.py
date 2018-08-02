
import urllib
import json
from bs4 import BeautifulSoup
from urllib.parse import quote
import time 

tags=[]
url='https://movie.douban.com/j/search_tags?type=movie'
request = urllib.request.Request(url)
response = urllib.request.urlopen(request, timeout=20)
result = json.loads((response.read()).decode('utf-8-sig'))

tags=result['tags']

movies=[]

for tag in tags:
	print(tag)
	limit = 0
	while 1:
		url = 'http://movie.douban.com/j/search_subjects?type=movie&tag=' + quote(tag) + \
		'&page_limit=20&page_start=' + str(limit)
		print(url)
		request = urllib.request.Request(url)
		response = urllib.request.urlopen(request, timeout=20)
		result = json.loads((response.read()).decode('utf-8'))

		result=result ['subjects']

		if len(result) == 0:
			break

		limit += 20
		for item in result:
			movies.append(item)
		break

	break

	print(len(movies))

for x in range(0,len(movies)):
	item =movies[x]
	request = urllib.request.Request(url=item['url'])
	response = urllib.request.urlopen(request, timeout=20)
	result = (response.read()).decode('utf-8')

	html = BeautifulSoup(result)
	
	try:
		description = html.find_all("span",attrs={"property": "v:summary"})[0].get_text().strip()
		print(description)
	except e:
		movies[x]['description'] = ''
	else:
		movies[x]['description'] = description
	finally:
		pass

	time.sleep(0.5)


fw = open('douban_movies.txy', 'w')
# 写入一行表头，用于说明每个字段的意义
fw.write('title^rate^url^cover^id^description\n')
for item in movies:
	# 用^作为分隔符
	# 主要是为了避免中文里可能包含逗号发生冲突
	fw.write(item['title'] + '^' + item['rate'] + '^' + item['url'] + '^' + item['cover'] + '^' + item['id'] + '^' + item['description'].strip() + '\n')
fw.close()