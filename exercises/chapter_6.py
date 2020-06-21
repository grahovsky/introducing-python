class Thing():
    pass

print(Thing)

example = Thing()
print(example)

class Thing2():
    letters = 'abc'

print(Thing2.letters)

class Thing3():
    def __init__(self):
        self.letters = 'xyz'

print(Thing3().letters)

class Element():
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number
    # def dump(self):
    #     print('{}, {}, {}'.format(self.name, self.symbol, self.number))
    def __str__(self):
        return '{}, {}, {}'.format(self.name, self.symbol, self.number)

element = Element('Hydrogen', 'H', 1)
print('{}, {}, {}'.format(element.name, element.symbol, element.number))

dict1 = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1}
hydrogen = Element(*dict1.values())
# hydrogen.dump()
print(hydrogen)

class Element_privacy():
    def __init__(self, name, symbol, number):
        self.__name = name
        self.__symbol = symbol
        self.__number = number

    @property
    def name(self):
        return self.__name

    @property
    def symbol(self):
        return self.__symbol

    @property
    def number(self):
        return self.__number

    def __str__(self):
        return '{}, {}, {}'.format(self.__name, self.__symbol, self.__number)

hydrogen_privacy = Element_privacy('Hydrogen privacy', 'H', 1)
print(hydrogen_privacy)
print(hydrogen.number)

class Bear():
    def eats(self):
        return 'berries'

class Rabbit():
    def eats(self):
        return 'clover'

class Octothorpe():
    def eats(self):
        return 'campers'

bear = Bear()
rabbit = Rabbit()
octo = Octothorpe()

print(bear.eats())
print(rabbit.eats())
print(octo.eats())

class Laser():
    def does(self):
        return 'disintegrate'

class Claw():
    def does(self):
        return 'crush'

class SmartPhone():
    def does(self):
        return 'ring'

class Robot():
    def __init__(self):
        self.laser = Laser()
        self.claw = Claw()
        self.smartPhone = SmartPhone()

    def does(self):
        return """I have many attachments:
My laser, to {}. 
My claw, to: {}.
My smartphone, to {}.""".format(
        self.laser.does(),
        self.claw.does(),
        self.smartPhone.does()
        )

robot = Robot()
print(robot.does())

