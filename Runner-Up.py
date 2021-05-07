def runnerup(n):

    lst = []
     #find out second maximum value
    while n>0:
        arr = input()
        lst.append(arr)
        n = n - 1

    first_maximum_value = max(lst[0],lst[1]) # 3
    second_maximum_value = min(lst[0], lst[1]) #2
    m = len(lst)
    for i in range(2, m):

        if lst[i] > first_maximum_value:
            second_maximum_value = first_maximum_value
            first_maximum_value = lst[i]
        elif lst[i] > second_maximum_value and first_maximum_value != lst[i]:
            second_maximum_value = lst[i]

    print((str(second_maximum_value)))

n = int(input())
runnerup(n)



# if __name__=="__main__":
#
#     n = int(input())
#
#     runnerup(n)

# lst = []
#     while n>0:
#         arr = (input())
#         lst.append(arr)
#         n = n - 1
#     print(lst)
