import numpy as np

# a = numpy.array([1,2,3,4,5])
#
# float_array = numpy.array([1,2,3,4,5,6], float)
# print(a)
# print(a[1:5])
#
# print(float_array)
#
# print(float_array[0])

take_input = list(map(int, input().split()))
# print(take_input)
np_array  = np.array(take_input, float)
l = len(np_array)

for i in range(1, l):
    print(np_array[l-i])
# print(np_array[::-1])