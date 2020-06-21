import re
result = re.match('You', 'Young Frankenstein')
print(result)

youpattern = re.compile('You')
result = youpattern.match('Young Frankenstein')
print(result)

source = 'Young Frankenstein'
m = re.match('You', source)  # match starts at the beginning of source
if m:  # match returns an object; do this to see what matched
    print(m.group())

source = 'Young Frankenstein'
m = re.match('Frank', source)
if m:
    print(m.group())
else:
    print('Frank don\'t match')

source = 'Young Frankenstein'
m = re.match('.*Frank.*', source)
if m:  # match returns an object
    print(m.group())

# Find First Match with search()
source = 'Young Frankenstein'
m = re.search('Frank', source)
if m:
     print(m.group())

# Find All Matches with findall()
source = 'Young Frankenstein'
m = re.findall('n.?', source)
print(m)

# Split at Matches with split()
source = 'Young Frankenstein'
m = re.split('n', source)
print(m)    # split returns a list

# Replace at Matches with sub()
source = 'Young Frankenstein'
m = re.sub('n', '?', source)
print(m)

# Patterns: Special Characters
import string
printable = string.printable
print(printable[0:50])
print(printable[50:])

print(re.findall('\d', printable)) # A single digit
print(re.findall('\D', printable)) # A single nondigit
print(re.findall('\w', printable)) # An alphanumeric character
print(re.findall('\W', printable)) # A non-alphanumeric character
print(re.findall('\s', printable)) # A whitespace character
print(re.findall('\S', printable)) # A nonwhitespace character
print(re.findall('\b', printable)) # A word boundary (between a \w and a \W, in either order)
print(re.findall('\B', printable)) # A nonword boundary


# Patterns: Using Specifiers
source = '''I wish I may, I wish I might
Have a dish of fish tonight.'''

print(re.findall('wish', source))
print(re.findall('wish|fish', source))
print(re.findall('^wish', source))
print(re.findall('^I wish', source))
print(re.findall('fish tonight.$', source))
print(re.findall('[wf]ish', source))
print(re.findall('[wsh]+', source))
print(re.findall('I (?=wish)', source))
print(re.findall('(?<=I) wish', source))

# Patterns: Specifying match() Output
m = re.search(r'(. dish\b).*(\bfish)', source)
print(m.group())
print(m.groups())

m = re.search(r'(?P<DISH>. dish\b).*(?P<FISH>\bfish)', source)
print(m.group())
# 'a dish of fish'
print(m.groups())
# ('a dish', 'fish')
print(m.group('DISH'))
# 'a dish'
print(m.group('FISH'))
# 'fish'