#!/usr/bin/python3

"""
This script fetches information about employee TODO lists from a REST API and exports it to a JSON file.
Usage: python3 3-dictionary_of_list_of_dictionaries.py
"""

import json
import requests

def fetch_employee_todo_data():
    base_url = "https://jsonplaceholder.typicode.com"
    users_url = f"{base_url}/users"

    try:
        users_response = requests.get(users_url)
        users_data = users_response.json()

        todo_data = {}

        for user in users_data:
            user_id = user["id"]
            user_name = user["username"]
            tasks_url = f"{base_url}/todos?userId={user_id}"
            tasks_response = requests.get(tasks_url)
            tasks_data = tasks_response.json()

            todo_data[str(user_id)] = []

            for task in tasks_data:
                todo_data[str(user_id)].append({
                    "username": user_name,
                    "task": task["title"],
                    "completed": task["completed"]
                })

        # Include all users in the output
        for user in users_data:
            if str(user["id"]) not in todo_data:
                todo_data[str(user["id"])] = []

        with open("todo_all_employees.json", "w") as json_file:
            json.dump(todo_data, json_file)

        print("Data exported to todo_all_employees.json")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    fetch_employee_todo_data()
