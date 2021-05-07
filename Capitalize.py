def test():


    i = input()

    str_split = i.split()
    e = []
    for i in range(len(str_split)):
    # print("{}".format(str_split[i].capitalize()))
        output = str_split[i].capitalize()
        e.append(output)
    return " ".join(e)


print(test())