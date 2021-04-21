def average(array):
    # your code goes here
    set_value = set(array)
    result = float(sum(set_value)) / float(len(set_value))
    r = round(result, 3)
    return r

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))


    result = average(arr)
    print(result)