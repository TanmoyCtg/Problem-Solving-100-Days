# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple

n = int(input())
fields =  input().split()
total = 0

for i in range(n):

    students = namedtuple('student', fields)
    ID, NAME, MARKS, CLASS = input().split()
    student = students(ID, NAME, MARKS, CLASS)
    total = total + int(student.MARKS)

result = total / n
print(round(result,2)    
