import sqlalchemy as sa

# in memory
conn = sa.create_engine('sqlite://')
# in file
#conn = sa.create_engine('sqlite:///sqlalchemy_base.db')

# The engine layer
conn.execute('''CREATE TABLE zoo
(critter VARCHAR(20) PRIMARY KEY,
count INT,
damages FLOAT)''')

ins = 'INSERT INTO zoo (critter, count, damages) VALUES (?, ?, ?)'
conn.execute(ins, 'duck', 10, 0.0)
conn.execute(ins, 'bear', 2, 1000.0)
conn.execute(ins, 'weasel', 1, 2000.0)

rows = conn.execute('SELECT * FROM zoo')

for row in rows:
    print(row)

# The SQL Expression Language
conn = sa.create_engine('sqlite://')

meta = sa.MetaData()
zoo = sa.Table('zoo', meta,
               sa.Column('critter', sa.String, primary_key=True),
               sa.Column('count', sa.Integer),
               sa.Column('damages', sa.Float)
               )

meta.create_all(conn)

conn.execute(zoo.insert(('bear', 2, 1000.0)))
conn.execute(zoo.insert(('weasel', 1, 2000.0)))
conn.execute(zoo.insert(('duck', 10, 0)))

result = conn.execute(zoo.select())

rows = result.fetchall()
print(rows)

# The Object-Relational Mapper (ORM)
# https://docs.sqlalchemy.org/en/13/orm/tutorial.html

from sqlalchemy.ext.declarative import declarative_base

conn = sa.create_engine('sqlite:///zoo.db')

Base = declarative_base()
print(type(Base))

class Zoo(Base):
    __tablename__ = 'zoo'
    critter = sa.Column('critter', sa.String, primary_key=True)
    count = sa.Column('count', sa.Integer)
    damages = sa.Column('damages', sa.Float)

    def __init__(self, critter, count, damages):
        self.critter = critter
        self.count = count
        self.damages = damages

    def __repr__(self):
        return "<Zoo({}, {}, {})>".format(self.critter, self.count, self.damages)


Base.metadata.create_all(conn)

# insert data by creating Python objects
first = Zoo('duck', 10, 0.0)
second = Zoo('bear', 2, 1000.0)
third = Zoo('weasel', 1, 2000.0)

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=conn)
print(type(Session))
session = Session()

# write the three objects
session.add(first)
session.add_all([second, third])

session.commit()

# sqlite3 zoo.db
# sqlite> .tables
# sqlite> select * from zoo;
