if __name__ == '__main__':
    N = int(input())
    empty_list = []

    while N>0:

        take_input = input().strip().split(" ")

        if take_input[0] == "append":
            empty_list.append(int(take_input[1]))
        elif take_input[0] == 'insert':
            empty_list.insert(int(take_input[1]), int(take_input[2]))
        elif take_input[0] == 'print':
            print(empty_list)
        elif take_input[0] == 'remove':
            empty_list.remove(int(take_input[1]))
        elif take_input[0] == 'sort':
            empty_list.sort()
        elif take_input[0] == 'pop':
            empty_list.pop()
        elif take_input[0] == 'reverse':
            empty_list.reverse()

        N = N -1
