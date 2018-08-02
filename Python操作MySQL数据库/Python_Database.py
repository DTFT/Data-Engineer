import MySQLdb
import MySQLdb.cursors



db = MySQLdb.connect(host='127.0.0.1', user='root', passwd='root', db='douban', port=3306, charset='utf8', cursorclass=MySQLdb.cursors.DictCursor)
db.autocommit(True)
cursor = db.cursor()

fr = open('douban_movie_clean.txt','r',encoding='utf-8',errors='ignore')

# Create
# count = 0
# for line in fr:
# 	count += 1
# 	print(count)
# 	if count == 1:
# 		continue
# 	line = line.strip().split('^')
# 	cursor.execute("insert into movie(tittle,url,rate,length,description) values (%s, %s, %s, %s, %s)",[line[1],line[2],line[4],line[-3],line[-1]])


# Update
# cursor.execute("update movie set tittle=%s, length=%s where id=1",['Alex','999'])

# # Read
# cursor.execute("select * from movie")
# movies = cursor.fetchall()
# # movies = cursor.fetchone()

# print (len(movies))
# print (movies[0])

# Delete
cursor.execute("delete from movie where id=%s",[1])



fr.close()

# 关闭数据库连接
cursor.close()
db.close()