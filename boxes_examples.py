from collections import defaultdict, Counter, OrderedDict


# Handle Missing Keys with setdefault() and defaultdict()
periodic_table = {'Hydrogen': 1, 'Helium': 2}
print(periodic_table)
сarbon = periodic_table.setdefault('Carbon', 12)
helium = periodic_table.setdefault('Helium', 111)

print(periodic_table)

bestiary = defaultdict(lambda: 'Huh?')
bestiary['E']
print(bestiary)


# Count Items with Counter()
breakfast = ['spam', 'spam', 'eggs', 'spam']
breakfast_counter = Counter(breakfast)

print(breakfast_counter)

print(breakfast_counter.most_common())
print(breakfast_counter.most_common(1))

lunch = ['eggs', 'eggs', 'bacon']
lunch_counter = Counter(lunch)
print(lunch_counter)

print(breakfast_counter + lunch_counter)

print(lunch_counter - breakfast_counter)
print(lunch_counter | breakfast_counter)


# Order by Key with OrderedDict()
quotes = OrderedDict([
    ('Moe', 'A wise guy, huh?'),
    ('Larry', 'Ow!'),
    ('Curly', 'Nyuk nyuk!')
])

for stooge, value in quotes.items():
    print('{}: {}'.format(stooge, value))

# Stack + Queue == deque
def palindrome(word):
    from collections import deque
    dq = deque(word)
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    return True

print(palindrome('radar'))
print(palindrome('halibut'))

# def another_palindrome(word):
#     return word == word[::-1]


# Iterate over Code Structures with itertools
import itertools

for item in itertools.chain([1,2], ['a', 'b']):
    print(item)

iter = 0

for item in itertools.cycle([1, 2]):
    print(item)
    iter += 1
    if iter > 20:
        break

for item in itertools.accumulate([1, 2, 3, 4]):
    print(item)

for item in itertools.accumulate([1, 2, 3, 4], lambda a, b: a * b):
    print(item)


# Print Nicely with pprint()
from pprint import pprint

print(quotes)
pprint(quotes)


# Get Random
from random import choice
print(choice([23, 9, 46, 'bacon', 0x123abc]))
print(choice(range(101)))
print(choice('alphabet'))

from random import sample
print(sample([23, 9, 46, 'bacon', 0x123abc], 3))
print(sample(range(101), 3))
print(sample('alphabet', 7))

from random import randint
print(randint(38, 74))

from random import randrange
print(randrange(38, 74))

from random import random
print(random())


