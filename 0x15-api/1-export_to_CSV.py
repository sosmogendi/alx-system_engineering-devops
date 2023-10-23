#!/usr/bin/python3

"""
This script fetches and displays information about an employee's TODO list progress and exports it to a CSV file.
Usage: python3 1-export_to_CSV.py <employee_id>
"""

import csv
import requests
import sys

def fetch_employee_todo_progress(employee_id):
    """
    Fetches and displays an employee's TODO list progress.
    """
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

        # Create a CSV file named USER_ID.csv
        csv_file_name = f"{user_id}.csv"

        with open(csv_file_name, mode="w", newline="") as csv_file:
            fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            writer.writeheader()
            for task in tasks_data:
                writer.writerow({
                    "USER_ID": user_id,
                    "USERNAME": employee_name,
                    "TASK_COMPLETED_STATUS": task["completed"],
                    "TASK_TITLE": task["title"]
                })

        print(f"Data exported to {csv_file_name}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    fetch_employee_todo_progress(employee_id)
