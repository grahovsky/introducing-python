# Python 3 Unicode Strings
import unicodedata

def unicode_test(value):
    name = unicodedata.name(value)
    value2 = unicodedata.lookup(name)
    print('value="%s", name="%s", value2="%s"' % (value, name, value2))

unicode_test('\u2603')

print(unicodedata.name('\u00e9'))

# UTF-8
snowman = '\u2603'
print('\u2603')
print(len(snowman))

ds = snowman.encode('utf-8')
print(ds)
print(len(ds))

# Decode
place = 'caf\u00e9'
print(place)
print(type(place))

place_bytes = place.encode('utf-8')
print(place_bytes)
print(type(place_bytes))

place2 = place_bytes.decode('utf-8')
print(place2)

try:
    place3 = place_bytes.decode('ascii')
    print(place3)
except Exception as err:
    print(err)

place4 = place_bytes.decode('latin-1')
print(place4)

place5 = place_bytes.decode('windows-1252')
print(place5)

# HTML Entities
import html
print(html.unescape("&egrave;"))
print(html.unescape("&#233;"))

place = 'caf\u00e9'
byte_value = place.encode('ascii', 'xmlcharrefreplace')
print(byte_value)
print(byte_value.decode())

# Formatting

# Old style: %
actor = 'Richard Gere'
cat = 'Chester'
weight = 28
print("My wife's favorite actor is %s" % actor)
print("Our cat %s weighs %s pounds" % (cat, weight))

thing = 9876
print('%d' % thing)
print('%12d' % thing)
print('%+12d' % thing)
print('%-12d' % thing)
print('%.3d' % thing)
print('%12.3d' % thing)
print('%-12.3d' % thing)

# New style: {} and format()
thing = 'woodchuck'
print('{}'.format(thing))

place = 'lake'
print('The {} is in the {}.'.format(thing, place))
print('The {1} is in the {0}.'.format(place, thing))

d = {'thing': 'duck', 'place': 'bathtub'}
print('The {0[thing]} is in the {0[place]}.'.format(d))

n = 42
f = 7.03
s = 'string cheese'
print('{0:^10d} {1:>10.4f} {2:<10s}'.format(n,f,s))
print('{0:!^30s}'.format('BIG SALE'))

# Newest Style: f-strings
thing = 'wereduck'
place = 'werepond'
print(f'The {thing} is in the {place}')
print(f'The {thing.capitalize()} is in the {place.rjust(20)}')
print(f'The {thing:>20} is in the {place:.^20}')

print(f'{thing = }, {place = }')
# thing = 'wereduck', place = 'werepond'
print(f'{thing[-4:] = }, {place.title() = }')
# thing[-4:] = 'duck', place.title() = 'Werepond'