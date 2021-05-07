'''
object oriented programming

'''

class Pet:

    def __init__(self, name, age):
        self.name =name
        self.age = age

    def show(self):
        print("I am {} and i am {} years old".format(self.name, self.age))

class Cat(Pet):
    def __init__(self, name, age, color):

        super().__init__(name, age) # call the super call and it's init attribute

        self.color = color
    def show(self):
        print("I am {} and i am {} years old and my body color is {}".format(self.name, self.age, self.color))
    def speak(self):
        print("meow")

class Dog(Pet):

    def speak(self):
        print("Bark")

p = Pet("Tim", 19)

p.show()

c = Cat("Billi", 35, "brown")

c.show()

class Person:
    number_of_people = 0
    def __init__(self):
        pass

P1 = Person()
Person.number_of_people=9
print(P1.number_of_people)

# static method don't change anything
