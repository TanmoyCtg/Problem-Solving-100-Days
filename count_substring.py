def count_substring(string, sub_string):
    count = 0
    s = len(string)
    for i in range(0,s):
        if string[i] in sub_string:
            count = count + 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)