import os
import csv

# 1
test1 = 'This is a test of the emergency text system'


with open('test.txt', 'wt') as fout:
    fout.write(test1)
# 2
with open('test.txt', 'rt') as fin:
    test2 = fin.read()
    print(test2 == test1)

# 3
text = '''author,book
J R R Tolkien,The Hobbit
Lynne Truss,"Eats, Shoots & Leaves"
'''

with open('books.csv', 'wt', newline='') as fout:
    fout.write(text)

# 4
with open('books.csv', 'rt', newline='') as fin:
    books = csv.DictReader(fin)
    for book in books:
        print(book)

# 5
text = '''title,author,year
The Weirdstone of Brisingamen,Alan Garner,1960
Perdido Street Station,China Mieville,2000
Thud!,Terri Pratchett,2005
The Spellman Files,Lisa Lutz,2007
Small Gods,Terry Pratchett,1992'''

with open('books.csv', 'wt', newline='') as fout:
    fout.write(text)

# 6
if os.path.exists('books.db'):
    os.remove('books.db')

import sqlite3
db = sqlite3.connect('books.db')
curs = db.cursor()

curs.execute('''CREATE TABLE books
    (title TEXT,
    author TEXT,
    year INT )
    ''')

# 7
ins_str = 'insert into books values(?, ?, ?)'
with open('books.csv', 'rt', newline='') as fin:
    books = csv.DictReader(fin)
    for book in books:
        curs.execute(ins_str, (book['title'], book['author'], book['year']))
    db.commit()

# 8
sql = 'SELECT title from books ORDER BY title ASC'
for row in db.execute(sql):
    print(row[0])

# 9
sql = 'SELECT * from books ORDER BY year ASC'
for row in db.execute(sql):
    print(*row, sep=', ')

# 10
import sqlalchemy
conn = sqlalchemy.create_engine('sqlite:///books.db')
sql = 'SELECT title FROM books ORDER BY title ASC'
rows = conn.execute(sql)
for row in rows:
    print(row)


# 11
import redis
conn = redis.Redis('arch-tc', 6379)

# conn.hset('test', {'count': 1, 'name': 'Fester Bestertester'})
conn.hset('test', 'count', 1, {'name': 'Fester Betertester'})
print(conn.hgetall('test'))

# 12
conn.hincrby('test', 'count', 3)
print(conn.hget('test', 'count'))