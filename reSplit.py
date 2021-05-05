import  re

s = input()
output =re.split(r"\D",s)

for i in output:
    print(i)

