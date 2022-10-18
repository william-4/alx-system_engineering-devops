#!/usr/bin/python3
""" A script that given an employee id
returns information about his/her TODO list progress.
"""

if __name__ == "__main__":
    import json
    import requests
    import sys

    url = 'https://jsonplaceholder.typicode.com/users/{}/todos'
    response_todos = requests.get(url.format(sys.argv[1]))
    response = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                            .format(sys.argv[1]))
    name = response.json().get("username")
    data = {}
    datalist = []

    for task in response_todos.json():
        datadict = {"task": task.get("title"), "completed": task.get(
                    "completed"), "username": name}
        datalist.append(datadict)

    data[sys.argv[1]] = datalist
    filename = sys.argv[1] + ".json"
    print(filename)

    with open(filename, mode='w') as f:
        json.dump(data, f)
