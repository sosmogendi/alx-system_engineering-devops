import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    tasks_url = f"{base_url}/todos?userId={employee_id}"

    try:
        user_response = requests.get(user_url)
        tasks_response = requests.get(tasks_url)
        user_data = user_response.json()
        tasks_data = tasks_response.json()

        employee_name = user_data.get("name")
        completed_tasks = [task for task in tasks_data if task["completed"]]
        total_tasks = len(tasks_data)

        print(f"Employee {employee_name} is done with tasks({len(completed_tasks)}/{total_tasks}):")
        for task in completed_tasks:
            print(f"\t{task['title']}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
