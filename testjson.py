import json, requests

response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos= json.loads(response.text)
# Map of userId to number of complete TODOs for that user
todos_by_user = {}

for todo in todos:
    if todo["completed"]:
        print(todo["userId"])