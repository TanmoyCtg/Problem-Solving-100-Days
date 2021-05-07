'''
- difference between arguments and parameters
- Positional and keyword arguments
- Default arguments
- variable-length arguments(*args and **kwargs)
-container unpacking into function arguments
- Local vs Global arguments
- Parameter Passing( by value or by reference?)

'''

# - difference between arguments and parameters

def print_name(name):
    # name is parameter
    print(name)

print_name('Alex') # here Alex is a arguments

# Positional and keyword arguments

def foo(a, b, c):
    print(a, b, c)

# foo(a=1, b =2 , c=3)  # keyword arguments a is keyword 1 is a value
# foo(c=9, b=4, a=2)

# foo(1, b=2, 3) # error

# Default arguments

def loo(a, b, c, d=5):
    print(a,b,c,d)

# loo(1,3,0)

# - variable-length arguments(*args and **kwargs)

def moo(a, b, *args, **kwargs):
    # kwargs = keyword arguments
    print(a,b)
    for arg in args:
        print(arg)
    for k, v in kwargs.items():
        print(k,v)

moo(1, 2, 3, 4, 5, six=6, seven=7)

def lol(a,b, *, c, d): # after * all parameter must be keyword arguments

    print(a, b, c, d)
lol(1, 2, c=3,d=4)

# container unpacking into function arguments

def unpack_var(a, b, c):
    print(a,b,c)

my_list= [1,2,3]
my_dict = {'a':1, 'b':2, 'c':3}
unpack_var(*my_list)
unpack_var(**my_dict)

# local vs global var

# param passing - call by obj reference
# mutable objects can be modified in a function

def modified_obj(a_list):
    return a_list.append(4)


my_list = [1,2,3]

modified_obj(my_list)

print(my_list)
def foo(x):
    x = 5

var = 10

foo(var)
print(var)

# ************* asterisk operator


my_tuple = (1,2,3)
my_list = [1,2,3]
my_dict = {1,2,3}
dict_a = {'a':1, 'b': 2}
dict_b = {'c':3, 'd':4}
new_dict = {**dict_a, **dict_b}

new_list = [*my_tuple, *my_list, *my_dict]


print(new_list, new_dict)


