gues_me = 7

if gues_me < 7:
    print('too low')
elif gues_me > 7:
    print('too high')
else:
    print('just right')

start = 1

while True:
    if start < gues_me:
        print('too low')
    elif start == gues_me:
        print('found it')
        break
    elif start > gues_me:
        print('oops')
        break
    start += 1

for value in [3, 2, 1, 0]:
    print(value)

even = [number for number in range(10) if number % 2 == 0]
print(even)

squares = {value: value**2 for value in range(10)}
print(squares)

odd = {number for number in range(10) if number % 2 == 1}
print(odd)

gen = ('Got ' + str(i) for i in range(10))

print(type(gen))

for thing in ('Got %s' % number for number in range(10)):
    print(thing)

def test(func):
    def new_function(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return new_function

def good() -> list:
    return ['Harry', 'Ron', 'Hermione']

@test
def get_odds():
    for number in range(1, 10, 2):
        yield number

for count, number in enumerate(get_odds(), 1):
    if count == 3:
        print("The third odd number is", number)
        break

class OopsException(Exception):
    print('Oops')


try:
    raise OopsException
except OopsException as exc:
    print('Caught an oops')

titles = ['Creature of Habbit', 'Crewel Fate']
plots = ['A nun turns into a monster', 'A haunted yarn shop']

movies = dict(zip(titles, plots))
print(movies)