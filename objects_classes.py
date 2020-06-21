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
    pass

give_me_a_car = Car()
give_me_a_yugo = Yugo()

# Methods
give_me_a_car.exclaim()
give_me_a_yugo.exclaim()
