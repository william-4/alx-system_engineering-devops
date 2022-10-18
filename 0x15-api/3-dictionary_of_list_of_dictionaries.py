#!/usr/bin/python3
""" A script that given an employee id
returns information about his/her TODO list progress.
"""

if __name__ == "__main__":
    import json
    import requests

    users = requests.get('https://jsonplaceholder.typicode.com/users')
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    users = users.json()
    todos = todos.json()

    data = {}

    for user in users:
        tasklist = []
        for task in todos:
            if task.get('userId') == user.get('id'):
                taskdict = {"username": user.get("username"), "task":
                            task.get("title"), "completed": task.get(
                                "completed")}
                tasklist.append(taskdict)

        data[user.get('id')] = tasklist

    with open("todo_all_employees.json", mode='w') as f:
        json.dump(data, f)
