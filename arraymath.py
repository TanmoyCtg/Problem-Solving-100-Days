# import numpy as np
# n,m = map(int,input().split())
#
# a=np.zeros((n,m),int)
# b=np.zeros((n,m),int)
#
# for i in range(n):
#   a[i]=np.array(input().split(),int)
# for i in range(n):
#   b[i]=np.array(input().split(),int)
# # print(a, b)
# print(a+b)
# print(a-b)
# print(a*b)
# print(np.array(a/b,int))
# print(a%b)
# print(a**b)

import numpy
numpy.set_printoptions(legacy='1.13')
my_array = numpy.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
# print (numpy.rint(my_array) )         #[  1.   2.   3.   4.   6.   7.   8.   9.  10.]

my_array = numpy.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
# print (numpy.floor(my_array))         #[ 1.  2.  3.  4.  5.  6.  7.  8.  9.]

x = list(map(float, input().split()))
# print(x)
print(numpy.floor(x))
print(numpy.ceil(x))
print(numpy.rint(x))