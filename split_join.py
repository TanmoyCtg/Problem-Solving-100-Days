def split_join(line):
    split_line = line.split()
    join_line = '-'.join(split_line)
    return join_line


if __name__ == '__main__':
    line = input()
    result = split_join(line)
    print(result)