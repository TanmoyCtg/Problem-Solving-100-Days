if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t = ()
    while n > 0:
        for i in integer_list:
            t = t+ (i,)

        n = n - 1
    print(hash(t))