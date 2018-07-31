encoding='utf8'

fr= open('xyj.txt','r',encoding='UTF-8')

characters = []
# 字典
stat = {}

# open方法，for line in f: print line #通过迭代器访问
for line in fr:
	line=line.strip()
	# 如果为空行则跳过该轮循环
	if len(line)==0 :
		continue    

	# 遍历该行的每一个字
	for x in range(0,len(line)):
		# 去掉标点符号和空白符
		if line[x] in [' ', '\t', '\n', '。', '，', '(', ')', '（', '）', '：', '□', '？', '！', '《', '》', '、', '；', '“', '”', '……']:
			continue
		# 尚未记录在characters中
		if not line[x] in characters:
			characters.append(line[x])
		# 尚未记录在stat中
		if line[x] not in stat:
			stat[line[x]] = 0
		# 汉字出现次数加1	
		stat[line[x]] += 1

	
print (len(characters))
print (len(stat))

# lambda生成一个临时函数
# d表示字典的每一对键值对，d[0]为key，d[1]为value
# reverse为True表示降序排序
stat = sorted(stat.items(), key=lambda d:d[1], reverse=True)

fw=open("result.csv","w",encoding= 'UTF-8-sig')
for item in stat:
	fw.write(item[0] + ',' + str(item[1]) + '\n')

fr.close()
fw.close()