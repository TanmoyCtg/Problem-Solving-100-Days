'''

lambda is a function one line func


'''

add10 = lambda x: x + 10
# i = int(input('enter value:'))
# print(' {}'.format(add10(int(input('enter value:')))))


points2D = [(1,2),(15,1), (5,-1), (10,4)]

points2D_sorted = sorted(points2D, key=lambda x: x[1])

print(points2D)
print(points2D_sorted)



a = [1, 2, 3, 4, 5]
b = map(lambda x: x*2, a)
l = list(b)

print(a)
print(b)



print(l)



# filter (func, seq)

f = filter(lambda x: x%2==0, a)
print(list(f))

y = [x for x in a if x%2!=0]

print(y)

# reduce(func, seq)

from functools import reduce

a = [1,2,3,4,5]

product_a = reduce(lambda x,y: x*y,a)

print(product_a)














