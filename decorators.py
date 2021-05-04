import functools

def start_end_decorator(func):

    @functools.wraps(func)
    def wrapper():

        print('Starting...')

        func()

        print('ending')

    return wrapper

def add_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("starting..")
        print("ending..")
        result = func(*args, **kwargs)
        return result

    return wrapper

@start_end_decorator
def print_name():
    print('iftekhar')

# send argument inside decorator function **kwargs , *args

@add_decorator
def add(x):
    return x+10
# result = add(24)
# print(result)
#
# print_name()

# print(help(add.__name__))




'''
# decorator with arguments 
this repeat decorator takes an argument and process it through decorator function.
it will show how many time it will call the function and print the value
'''
def repeat(num_times):

    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat

@repeat(num_times = 4)
def greet(name, lastname='joy'):
    print('Hello {} {}'.format(name, lastname))


greet('Iftekhar', 'chowdhury')

# nested decorators

# class decorator maintain update an state

class CountCalls:

    def __init__(self, func):
        self.func = func
#       create an state how many times it calls
        self.num_calls = 0
    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print("this is executed {} times".format(self.num_calls))
        return self.func(*args, **kwargs)

@CountCalls
def say_hello():
    print("Hello")

say_hello()
say_hello()
say_hello()
say_hello()

# execution time of function
# debug decortaor
# check decorator -
# register function
# add information or update the state


################################# make a sentence uppercase need to write a decorator for that#######################

''' 
we pass say_hi function to the uppercase_decorator as an argument 
'''
def uppercase_decorator(function):

    def wrapper():
        func = function()
        d = dir(func)
        t = type(func)
        make_uppercase = func.upper()
        # return (d, t, make_uppercase)
        return make_uppercase
    return wrapper

def split_string(function):

    def wrapper():

        func = function()
        split_str = func.split()
        return split_str
    return wrapper



def remove_space(function):
    def wrapper():

        func = function()
        return dir(func)
    return wrapper


# same things other ways
#  we use multiple decorator for one functions
#  multiple decorator process one by one

# @remove_space
@split_string
@uppercase_decorator
def say_hi():
    return 'hello joy'

print(say_hi())
decorator = uppercase_decorator(say_hi)
# print(decorator())

####### decorator with arguments ####################
def decorator_with_arguments(function):

    def wrapper_with_arguments(arg1, arg2):
        print('my arguments are {} and {}'.format(arg1, arg2))
        function(arg1, arg2)
    return wrapper_with_arguments

@decorator_with_arguments
def cities(city_one, city_two):
    print("i love these cities {} and {}".format(city_one, city_two))

cities("CTG", "LA")

#### Defining General Purpose Decorators#########

def a_decorator_passing_arbitrary_arguments(function_to_decorate):
    def a_wrapper_accepting_arbitrary_arguments(*args,**kwargs):
        print('The positional arguments are', args)
        print('The keyword arguments are', kwargs)
        function_to_decorate(*args)
    return a_wrapper_accepting_arbitrary_arguments

@a_decorator_passing_arbitrary_arguments
def function_with_no_argument():
    print("No arguments here.")
@a_decorator_passing_arbitrary_arguments
def function_with_argument(a, b, c):
    print(a, b, c)
function_with_no_argument()
function_with_argument(1,2,3)

@a_decorator_passing_arbitrary_arguments
def function_with_keyword_arguments():
    print("This has shown keyword arguments")

function_with_keyword_arguments(first_name="Derrick", last_name="Mwiti")

def decorator_maker_with_arguments(decorator_arg1, decorator_arg2, decorator_arg3):
    def decorator(func):
        def wrapper(function_arg1, function_arg2, function_arg3) :
            "This is the wrapper function"
            print("The wrapper can access all the variables\n"
                  "\t- from the decorator maker: {0} {1} {2}\n"
                  "\t- from the function call: {3} {4} {5}\n"
                  "and pass them to the decorated function"
                  .format(decorator_arg1, decorator_arg2,decorator_arg3,
                          function_arg1, function_arg2,function_arg3))
            return func(function_arg1, function_arg2,function_arg3)

        return wrapper

    return decorator

pandas = "Pandas"
@decorator_maker_with_arguments(pandas, "Numpy","Scikit-learn")
def decorated_function_with_arguments(function_arg1, function_arg2,function_arg3):
    print("This is the decorated function and it only knows about its arguments: {0}"
           " {1}" " {2}".format(function_arg1, function_arg2,function_arg3))

decorated_function_with_arguments(pandas, "Science", "Tools")
