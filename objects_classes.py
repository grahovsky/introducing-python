# Define a Class with class
class Person():
    # Initialization
    def __init__(self, name):
        self.name = name

hunter = Person('Elmer Fudd')

# Attributes
print('The mighty hunter:', hunter.name)

# Inheritance
class Car():
    def exclaim(self):
        print("I'm a Car!")

class Yugo(Car):
    #pass
    # Override a Method
    def exclaim(self):
        print("I'm a Yugo! Much like a Car, but more Yugo-ish.")

    # Add a Method
    def need_a_push(self):
        print("A little help here?")

give_me_a_car = Car()
give_me_a_yugo = Yugo()

# Methods
give_me_a_car.exclaim()
give_me_a_yugo.exclaim()
give_me_a_yugo.need_a_push()

class MDPerson(Person):
    # Override a Method
    def __init__(self, name):
        self.name = "Doctor " + name

doctor = MDPerson('Fudd')
print(doctor.name)

# Get Help from Your Parent with super()
class EmailPerson(Person):
    def __init__(self, name, email):
        super().__init__(name)
        self.email = email

bob = EmailPerson('Bob Frapples', 'bob@frapples.com')

print('{}: {}'.format(bob.name, bob.email))


# Multiple Inheritance
class Animal:
     def says(self):
         return 'I speak!'

class Horse(Animal):
     def says(self):
         return 'Neigh!'

class Donkey(Animal):
     def says(self):
         return 'Hee-haw!'

class Mule(Donkey, Horse):
     pass

class Hinny(Horse, Donkey):
     pass

# __mro__
print(Mule.mro())
print(Hinny.mro())

mule = Mule()
hinny = Hinny()
print(mule.says())
print(hinny.says())

# Mixins
class PrettyMixin():
    def dump(self):
        import pprint
        pprint.pprint(vars(self))

class Thing(PrettyMixin):
    pass

t = Thing()
t.name = "Nyarlathotep"
t.feature = "ichor"
t.age = "eldritch"
t.dump()

# Attribute Access, Getters and Setters
class Duck():
    def __init__(self, input_name):
        # self.hidden_name = 'duck ' + input_name
        # Name Mangling for Privacy
        self.__name = 'duck ' + input_name
    def get_name(self):
        print('inside the getter')
        return self.__name
    def set_name(self, input_name):
        print('inside the setter')
        self.__name = 'duck ' + input_name
    name = property(get_name, set_name)

fowl = Duck('Howard')
print(fowl.name)

fowl.name = 'Daffy'
print(fowl.name)

# Name Mangling for Privacy
fowl._Duck__name = 'duck privacy Daffy'
print('privacy __name', fowl._Duck__name)

# In the second method, you add some decorators and replace the method names get_name and set_name with name:
class Chiken():
    def __init__(self, input_name):
        self.__name = 'chicken ' + input_name
    @property
    def name(self):
        print('inside the getter')
        return self.__name
    @name.setter
    def name(self, input_name):
        print('inside the setter')
        self.__name = 'chicken ' + input_name

chic = Chiken('Howard')
print(chic.name)
fowl.name = 'Donald'
print(chic.name)

class Circle():
    def __init__(self, radius):
        self.radius = radius
    @property
    def diameter(self):
        return 2 * self.radius

c = Circle(5)
print(c.radius)
print(c.diameter)

# Class Methods
class A():
    count = 0
    def __init__(self):
        A.count += 1
    def exclaim(self):
        print("I'm an A!")
    @classmethod
    def kids(cls):
        print("A has", cls.count, "little objects.")

easy_a = A()
breezy_a = A()
wheezy_a = A()

A.kids()

# Static Methods
class CoyoteWeapon():
    @staticmethod
    def commercial():
        print('This CoyoytWeapon has been brought to you by Acme')

CoyoteWeapon.commercial()

# Duck Typing
class Quote():
    def __init__(self, person, words):
        self.person = person
        self.words = words
    def who(self):
        return self.person
    def says(self):
        return self.words + '.'

class QuestionQuote(Quote):
     def says(self):
         return self.words + '?'

class ExclamationQuote(Quote):
     def says(self):
         return self.words + '!'

hunter = Quote('Elmer Fudd', "I'm hunting wabbits")
hunted1 = QuestionQuote('Bugs Bunny', "What's up, doc")
hunted2 = ExclamationQuote('Daffy Duck', "It's rabbit season")

class BabblingBrook():
    def who(self):
        return 'Brook'
    def says(self):
        return 'Babble'

brook = BabblingBrook()

def who_says(obj):
    print(obj.who(), 'says', obj.says())

who_says(hunter)
who_says(hunted1)
who_says(hunted2)
who_says(brook)

# Magic Methods
class Word():
    def __init__(self, text):
        self.text = text
    def __eq__(self, word2):
        return self.text.lower() == word2.text.lower()

first = Word('ha')
second = Word('HA')
third = Word('eh')
print(first == second)
print(first == third)

class Word2():
    def __init__(self, text):
        self.text = text
    def __eq__(self, word2):
        return self.text.lower() == word2.text.lower()
    def __str__(self):
        return self.text
    def __repr__(self):
        return 'Word("'  + self.text  + '")'

first = Word2('ha')
#>>>first          # uses __repr__
print(first)   # uses __str__


# Composition
class Bill():
    def __init__(self, description):
        self.description = description

class Tail():
    def __init__(self, length):
        self.length = length

class Duck():
    def __init__(self, bill, tail):
        self.bill = bill
        self.tail = tail
    def about(self):
        print('This duck has a', self.bill.description,
            'bill and a', self.tail.length, 'tail')

a_tail = Tail('long')
a_bill = Bill('wide orange')
duck = Duck(a_bill, a_tail)
duck.about()

# Named Tuples
from collections import namedtuple
Duck = namedtuple('Duck', 'bill tail')
duck = Duck('wide orange', 'long')
print(duck)
print(duck.bill)
print(duck.tail)

parts = {'bill': 'wide orange', 'tail': 'long'}
duck2 = Duck(**parts)
print(duck2)

duck3 = duck2._replace(tail='magnificent', bill='crushing')
print(duck3)

# Dataclasses
from dataclasses import dataclass
@dataclass
class AnimalClass:
    name: str
    habitat: str
    teeth: int = 0

snowman = AnimalClass('yeti', 'Himalayas', 46)
duck = AnimalClass(habitat='lake', name='duck')
print(snowman)
print(duck)