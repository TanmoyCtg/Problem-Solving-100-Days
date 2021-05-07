if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    sum =0
    for i in student_marks[query_name]:

        sum = sum + i
    result = float(sum) / float(len(scores))
    result = float(result)
    # print(round(result,2))
    print(format(result, '.2f'))