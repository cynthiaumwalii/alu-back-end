#!/usr/bin/python3

import requests

URL = "https://jsonplaceholder.typicode.com/users"

def gather_data(user_id):
    employee_data = requests.get(f"{URL}/{user_id}")
    employee_name = employee_data.json()["name"]
    response = requests.get(f"{URL}/{user_id}/todos")
    data = response.json()
    completed_count = 0
    completed_tasks = []
    total_tasks = len(data)
    for item in data:
        if item["completed"]:
            completed_count += 1
            completed_tasks.append(item["title"])

    print(f"Employee {employee_name} is done with {completed_count}/{total_tasks}")
    for compl_itm in completed_tasks:
        print(f"\t{compl_itm}")

gather_data(1)