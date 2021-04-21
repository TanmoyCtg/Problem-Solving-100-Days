'''
find out the distinct country from sets and show their count

remove the space
all the inputs country saved in a list
then make it set
return the len of set

'''
def distinct_country (array):
    t = set(array)
    return len(t)

if __name__ == '__main__':
    n = int(input())
    empty_list = []
    for _ in range(n):
        country = input().strip()
        country_list = empty_list.append(country)

    result = distinct_country(empty_list)
    print(result)

