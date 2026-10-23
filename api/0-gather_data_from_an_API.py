#!/usr/bin/python3
"""Gather an employee's TODO progress from a REST API."""

import requests
import sys

URL = "https://jsonplaceholder.typicode.com/users"

user_id = sys.argv[1]

employee_name = requests.get(f"{URL}/{user_id}").json()["name"]
data = requests.get(f"{URL}/{user_id}/todos").json()

completed_tasks = [item["title"] for item in data if item["completed"]]

print(f"Employee {employee_name} is done with tasks"
      f"({len(completed_tasks)}/{len(data)}):")
for title in completed_tasks:
    print(f"\t {title}")