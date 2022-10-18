#!/usr/bin/python3
""" A script that given an employee id
returns information about the employee in csv format..
"""

if __name__ == "__main__":
    import csv
    import requests
    import sys

    response_todos = requests.get("https://jsonplaceholder.typicode.com/users/"
                                  "{}/todos".format(sys.argv[1]))
    response = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                            .format(sys.argv[1]))
    name = response.json().get("username")
    filename = sys.argv[1] + ".csv"
    with open(filename, mode='w') as f:
        writer = csv.writer(f, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_ALL, lineterminator='\n')
        for task in response_todos.json():
            writer.writerow([sys.argv[1], name, str(task.get('completed')),
                             task.get('title')])
