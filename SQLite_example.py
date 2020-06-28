import sqlite3

conn = sqlite3.connect('enterprise.db')
curs = conn.cursor()


def checkTableExists(dbcon, tablename):
    curs = dbcon.cursor()
    curs.execute('''SELECT count(name) 
    FROM sqlite_master 
    WHERE type='table' AND name='{0}'
    '''.format(tablename.replace('\'', '\'\'')))

    if curs.fetchone()[0] == 1:
        curs.close()
        return True

    curs.close()
    return False

tableZooExists = checkTableExists(conn, 'zoo')

if not tableZooExists:

    curs.execute('''CREATE TABLE zoo
    (critter VARCHAR(20) PRIMARY KEY,
    count INT,
    damages FLOAT)
    ''')

    # add some animals to the zoo:
    curs.execute('INSERT INTO zoo VALUES("duck", 5, 0.0)')
    curs.execute('INSERT INTO zoo VALUES("bear", 2, 1000.0)')

    # use a placeholder:
    ins = 'INSERT INTO zoo (critter, count, damages) VALUES(?, ?, ?)'
    curs.execute(ins, ('weasel', 1, 2000.0))

    # for SAVA data
    conn.commit()

# get all our animals
curs.execute('SELECT * FROM zoo')
rows = curs.fetchall()
print(rows)

# ordered by their counts:
curs.execute('SELECT * from zoo ORDER BY count')
print(curs.fetchall())

# descending order
curs.execute('SELECT * from zoo ORDER BY count DESC')
print(curs.fetchall())

# most costing animals
curs.execute('''SELECT * FROM zoo WHERE
damages = (SELECT MAX(damages) FROM zoo)''')
print(curs.fetchall())

curs.close()
conn.close()

