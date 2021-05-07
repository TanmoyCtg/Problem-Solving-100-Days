import numpy

i = int(input())

l = []
while i > 0:

    row = map(float, input().split())
    l.append(row)
    # l.append([a])
    i = i - 1
print(l)
for i in l:
    print(i)

# result = numpy.linalg.det(l)
# print(round(result,2))


