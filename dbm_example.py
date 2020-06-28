import dbm


db = dbm.open('definitions', 'c')   # 'r' to read, 'w' to write, and 'c' for both

db['mustard'] = 'yellow'
db['ketchup'] = 'red'
db['pesto'] = 'green'

print(db['pesto'])

db.close()
db = dbm.open('definitions', 'r')
print(db['mustard'])