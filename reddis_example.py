# pip install redis
import redis

conn = redis.Redis('arch-tc', 6379)
print(conn.keys('*'))

conn.set('secret', 'ni!')
conn.set('carats', 24)
conn.set('fever', '101.5')

print(conn.get('secret'))
print(conn.get('carats'))
print(conn.get('fever'))

# sets a value only if the key does not exist
conn.setnx('secret', 'icky-icky-boing!')

# The getset() method returns the old value and sets it to a new one at the same time:
print(conn.getset('secret', 'icky-icky-boing!'))
print(conn.get('secret'))
print(conn.getrange('secret', -6, -1))

# Replace a substring by using setrange() (using a zero-based offset):
conn.setrange('secret', 0, 'ICKY')
print(conn.get('secret'))

# set multiple keys at once by using mset():
conn.mset({'pie': 'cherry', 'cordial': 'sherry'})

# Get more than one value at once by using mget():
print(conn.mget(['fever', 'pie']))

# Delete a key by using delete():
conn.delete('fever')

# Increment, decrement
conn.incr('carats')
conn.incr('carats', -2)
conn.decr('carats')
conn.decr('carats', 15)
print(conn.get('carats'))

conn.set('fever', '101.5')
conn.incrbyfloat('fever', -1.5)
print(conn.get('fever'))

# Lists
# Redis lists can contain only strings.
conn.delete('zoo')

# Insert more than one item at the beginning:
conn.lpush('zoo', 'bear')
conn.lpush('zoo', 'alligator', 'duck')

# Insert before or after a value by using linsert():
conn.linsert('zoo', 'before', 'bear', 'beaver')
conn.linsert('zoo', 'after', 'bear', 'cassowary')

# Insert at an offset by using lset() (the list must exist already):
conn.lset('zoo', 2, 'marmoset')

# Insert at the end by using rpush():
conn.rpush('zoo', 'yak')

# Get the value at an offset by using lindex():
print(conn.lindex('zoo', 3))

# Get the values in an offset range by using lrange() (0 to -1 for all):
print(conn.lrange('zoo', 0, -1))

# Get the values in an offset range by using lrange() (0 to -1 for all):
conn.ltrim('zoo', 1, 4)
print(conn.lrange('zoo', 0, -1))


# Hashes
# Redis hashes are similar to Python dictionaries but can contain only strings.

# Set the fields do and re in hash song at once by using hmset(): DEPRICATED
# conn.hmset('song', {'do': 'a deer', 're': 'about a deer'})

# Set a single field value in a hash by using hset():
conn.hset('song', 'mi', 'a note to follow re')
conn.hset('song', 'do', 'a deer')

# Get one field’s value by using hget():
print(conn.hget('song', 'mi'))

# Get multiple field values by using hmget():
print(conn.hmget('song', 'mi', 'do'))

# Get all field keys for the hash by using hkeys():
print(conn.hkeys('song'))

# Get all field values for the hash by using hvals():
print(conn.hvals('song'))

# Get the number of fields in the hash by using hlen():
print(conn.hlen('song'))

# Get all field keys and values in the hash by using hgetall():
print(conn.hgetall('song'))

# Set a field if its key doesn’t exist by using hsetnx():
conn.hsetnx('song', 'fa', 'a note that rhymes with la')
conn.delete('zoo')

# Sets

# Add one or more values to a set:
conn.sadd('zoo', 'duck', 'goat', 'turkey')

# Get the number of values from the set:
print(conn.scard('zoo'))

# Get the number of values from the set:
print(conn.smembers('zoo'))

# Remove a value from the set:
conn.srem('zoo', 'turkey')
print(conn.smembers('zoo'))

# Let’s make a second set to show some set operations:
conn.sadd('better_zoo', 'tiger', 'wolf', 'duck')

# Intersect (get the common members of) the zoo and better_zoo sets:
print(conn.sinter('zoo', 'better_zoo'))

# Get the intersection of zoo and better_zoo, and store the result in the set fowl_zoo:
conn.sinterstore('fowl_zoo', 'zoo', 'better_zoo')
print(conn.smembers('fowl_zoo'))

# Get the union (all members) of zoo and better_zoo:
print(conn.sunion('zoo', 'better_zoo'))

# Store that union result in the set fabulous_zoo:
conn.sunionstore('fabulous_zoo', 'zoo', 'better_zoo')
print(conn.smembers('fabulous_zoo'))

# What does zoo have that better_zoo doesn’t? Use sdiff() to get the set difference, and sdiffstore() to save it in the zoo_sale set:
print(conn.sdiff('zoo', 'better_zoo'))
conn.sdiffstore('zoo_sale', 'zoo', 'better_zoo')
print(conn.smembers('zoo_sale'))


# Sorted sets
import time
now = time.time()
print(now)

conn.zadd('logins', {'smeagol': now})
conn.zadd('logins', {'sauron': now+(5*60)})
conn.zadd('logins', {'bilbo': now+(2*60*60)})
conn.zadd('logins', {'treebeard': now+(24*60*60)})

# In what order did bilbo arrive?
print(conn.zrank('logins', 'bilbo'))

# When was that?
print(conn.zscore('logins', 'bilbo'))

# Let’s see everyone in login order:
print(conn.zrange('logins', 0, -1))

# With their times, please:
print(conn.zrange('logins', 0, -1, withscores=True))

# Bits
days = ['2013-02-25', '2013-02-26', '2013-02-27']
big_spender = 1089
tire_kicker = 40459
late_joiner = 550212

conn.setbit(days[0], big_spender, 1)
conn.setbit(days[0], tire_kicker, 1)

# next day
conn.setbit(days[1], big_spender, 1)

# next day
conn.setbit(days[2], big_spender, 1)
conn.setbit(days[2], late_joiner, 1)

for day in days:
    print(conn.bitcount(day))

print(conn.getbit(days[1], tire_kicker))

print(conn.bitop('and', 'everyday', *days))
print(conn.bitcount('everyday'))

print(conn.getbit('everyday', big_spender))

conn.bitop('or', 'alldays', *days)
print(conn.bitcount('alldays'))


# Caches and expiration
print('\n','{0:!^30s}'.format('caches adn expiration'))

key = 'now you see it'
conn.set(key, 'but not for long')

conn.expire(key, 5)
print(conn.ttl(key))

print(conn.get(key))

time.sleep(6)
print(conn.get(key))