import random

a = random.random()

b = random.randint(1,10)

print(a,b)

myList = list('ABCDaecdEe')

c = random.choice(myList)
print(c)

random.shuffle(myList)
print(myList)

random.seed(1)
print(random.random())
print(random.randint(1,10))

random.seed(2)
print(random.random())
print(random.randint(1,10))

random.seed(3)
print(random.random())
print(random.randint(1,10))

random.seed(4)
print(random.random())
print(random.randint(1,10))

