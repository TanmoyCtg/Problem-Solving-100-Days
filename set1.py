'''
find the average of set values

this problem take the list make it set using set()

then we calculate the sum of set value and divided by len of set value,

round up 3 digit and return the value

'''
def average(array):
    # your code goes here
    set_value = set(array)
    result = float(sum(set_value)) / float(len(set_value))
    r = round(result, 3)
    return r

