#!/usr/bin/python3
"""ALX SE API INTRO."""
import requests
from sys import argv


def main() -> int:
    """Return information about a user TODO list progress."""
    base_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])
    todo_url = '{}/todos'.format(base_url)
    res = requests.get(todo_url)
    if res.status_code == 200:
        res = res.json()
        name = requests.get(base_url).json().get('name')
        completed_tasks = [val for val in res if val["completed"]]
        length = len(completed_tasks)
        total = len(res)
        print('Employee {} is done with tasks({}/{}):'.format(
            name, length,
            total))
        for task in completed_tasks:
            print('\t {}'.format(task['title']))
    return 0


if __name__ == '__main__':
    main()
