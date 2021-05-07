import re

text = "house number: 5, phone number: 017 11101001"
match = re.search('\d{3}\s*\d{8}',text)

# print(match.group())

# whitespace \s* meaning of star - maybe zero or more space
# \s+ - one or more space

# \d{3}\s*\d{8}


text1 = 'my roll number: 1 1'
r = re.search('\d{1}\s*\d{1}',text1)


text2= "multiple phone number, 01711111111, 01819998298, 01543903912"
result = re.findall(r'01[56789]\s*\d{8}', text2)

# print(result)

str_a = 'ABCDCDC'

match1 = re.search('ABCD\w+h', str_a)

# print(type(match1))
# print(match1.group())

# ^ - start & $ - end

s = "bangla english bangla"

pattern = 'CDC'

count = 0
left =0
while True:
    match2 = re.search(pattern, str_a[left:])

    if not match2:
        break
    count = count + 1
    left = left + match2.start()+1


print(count)

import  requests

print(dir(requests))
res = requests.get('http://inventwithpython.com/page_that_does_not_exist')
print(res.raise_for_status() )
