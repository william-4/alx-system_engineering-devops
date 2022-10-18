#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""

if __name__ == "__main__":
    import requests
    import sys

    url = "https://jsonplaceholder.typicode.com/users/"
    user_todos = requests.get(url + "{}/todos".format(sys.argv[1]))
    user = requests.get(url + "{}".format(sys.argv[1]))

    name = user.json().get("name")
    tasks_total = len(user_todos.json())
    tasks_completed = []
    for task in user_todos.json():
        if task.get("completed"):
            tasks_completed.append(task.get("title"))

    num_completed = len(tasks_completed)
    print("Employee {} is done with tasks({}/{}):"
          .format(name, num_completed, tasks_total))
    for title in tasks_completed:
        print("\t {}".format(title))
