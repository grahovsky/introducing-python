gues_me = 7

if gues_me < 7:
    print('too low')
elif gues_me > 7:
    print('too high')
else:
    print('just right')

start = 1

while start < gues_me:
    print(start)
    start += 1
else:
    print("found it!")

list_1 = [i for i in range(3,-1,-1)]

for i in list_1:
    print(i)

list_2 = [i for i in range(10) if i % 2 == 1]

print(list_2)

squares = {value: value**2 for value in range(10)}
print(squares)

odd = {i for i in range(10) if i % 2 == 0}
print(odd)

gen = ('Got ' + str(i) for i in range(10))

print(type(gen))

for gen_item in gen:
    print(gen_item)

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
    return [i for i in range(10) if i % 2 == 0]

odds = get_odds()

print(odds[2])

class OopsException(Exception):
    print('Oops')


try:
    raise OopsException
except OopsException as exc:
    print(exc)

titles = ['Creature of Habbit', 'Crewel Fate']
plots = ['A nun turns into a monster', 'A haunted yarn shop']

movies = dict(zip(titles, plots))

print(movies)