'''
The process of encoding JSON is usually called serialization


'''

import  json,pprint , requests

person = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "hasChildren": False,
    "titles": ['engineer', 'programmer']
}

# print(pprint.pprint(person))
#
# print(type(person))

# how to make json convert from dict

personJson = json.dumps(person, indent=4, sort_keys=True)

# print(type(personJson))
# print(personJson)

response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos= json.loads(response.text)
# Map of userId to number of complete TODOs for that user
todos_by_user = {}

for todo in todos:
    if todo["completed"]:
        try:
            todos_by_user[todo["userId"]] += 1
        except KeyError:
            todos_by_user[todo["userId"]] =1

# print(todos_by_user)
top_users = sorted(todos_by_user.items(), key=lambda x: x[1], reverse=True)
print(top_users)
max_complete = top_users[0][1]

print(max_complete)

# Create a list of all users who have completed
# the maximum number of TODOs.
users = []
for user, num_complete in top_users:
    if num_complete < max_complete:
        break
    users.append(str(user))

max_users = " and ".join(users)



def keep(todo):

    is_complete = todo['completed']
    has_max_count = str(todo["userId"]) in users
    return is_complete and has_max_count

with open('filtered_data_file.json', 'w') as data_file:

    filtered_todos = list(filter(keep, todos))
    json.dump(filtered_todos, data_file, indent=2)

# print(todos)
# print(type(todos))