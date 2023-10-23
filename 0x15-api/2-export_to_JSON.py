#!/usr/bin/python3

"""
This script fetches and displays information about an employee's TODO list progress and exports it to a JSON file.
Usage: python3 2-export_to_JSON.py <employee_id>
"""

import json
import requests
import sys

def fetch_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    tasks_url = f"{base_url}/todos?userId={employee_id}"

    try:
        user_response = requests.get(user_url)
        tasks_response = requests.get(tasks_url)
        user_data = user_response.json()
        tasks_data = tasks_response.json()

        employee_name = user_data.get("name")
        user_id = user_data.get("id")

        json_data = {str(user_id): []}
        for task in tasks_data:
            json_data[str(user_id)].append({
                "task": task["title"],
                "completed": task["completed"],
                "username": employee_name
            })

        # Create a JSON file named USER_ID.json
        json_file_name = f"{user_id}.json"
        with open(json_file_name, "w") as json_file:
            json.dump(json_data, json_file, indent=4)

        print(f"Data exported to {json_file_name}")

        if len(json_data[str(user_id)]) != 20:
            sys.exit(1)

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    fetch_employee_todo_progress(employee_id)
