students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

# print('{} {} {} {}'.format(students[0], students[1], students[0][0], students[0][1]))

if __name__ == '__main__':
    emp_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        name_list = name.split()
        name_list.append(score)
        emp_list.append(name_list)

    first_max_score = emp_list[0][1]  # 37.21
    second_max_score = emp_list[1][1]  # 37.21



    n = len(emp_list)

    for i in range(2, n):

        if emp_list[i][i-1] > first_max_score:
            second_max_score = first_max_score
            first_max_score = emp_list[i][i-1]
        elif emp_list[i][i-1] > second_max_score and first_max_score != emp_list[i][i-1]:
            second_max_score = emp_list[i][i-1]

    print(second_max_score)


    # print(emp_list)
    # print(a)