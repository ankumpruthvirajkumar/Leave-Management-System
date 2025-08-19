import datetime

class LeaveManagementSystem:
    def __init__(self):
        self.employees = {}
        self.leave_requests = {}
        self.next_employee_id = 1
        self.next_leave_request_id = 1

    def add_employee(self, name, email, department, joining_date_str):
        try:
            joining_date = datetime.datetime.strptime(joining_date_str, "%Y-%m-%d").date()
            employee_id = self.next_employee_id
            self.employees[employee_id] = {
                "name": name,
                "email": email,
                "department": department,
                "joining_date": joining_date,
                "leave_balance": 20  # Assumption: Initial leave balance is 20 days
            }
            self.next_employee_id += 1
            print(f"Employee {name} added successfully with ID: {employee_id}")
            return employee_id
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
            return None

    def apply_for_leave(self, employee_id, start_date_str, end_date_str):
        if employee_id not in self.employees:
            print("Error: Employee not found.")
            return

        employee = self.employees[employee_id]

        try:
            start_date = datetime.datetime.strptime(start_date_str, "%Y-%m-%d").date()
            end_date = datetime.datetime.strptime(end_date_str, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
            return

        # Edge Case: Applying for leave before joining date
        if start_date < employee["joining_date"]:
            print("Error: Cannot apply for leave before the joining date.")
            return

        # Edge Case: Invalid dates (end date before start date)
        if end_date < start_date:
            print("Error: End date cannot be before the start date.")
            return

        leave_days = (end_date - start_date).days + 1

        # Edge Case: Applying for more days than available balance
        if leave_days > employee["leave_balance"]:
            print("Error: Insufficient leave balance.")
            return

        # Edge Case: Overlapping leave requests
        for req_id, request in self.leave_requests.items():
            if request["employee_id"] == employee_id and request["status"] != "Rejected":
                req_start = request["start_date"]
                req_end = request["end_date"]
                if (start_date <= req_end) and (end_date >= req_start):
                    print("Error: Overlapping leave request found.")
                    return

        leave_request_id = self.next_leave_request_id
        self.leave_requests[leave_request_id] = {
            "employee_id": employee_id,
            "start_date": start_date,
            "end_date": end_date,
            "days": leave_days,
            "status": "Pending"
        }
        self.next_leave_request_id += 1
        print(f"Leave request submitted successfully with ID: {leave_request_id}")

    def approve_or_reject_leave(self, leave_request_id, new_status):
        if leave_request_id not in self.leave_requests:
            print("Error: Leave request not found.")
            return

        if new_status not in ["Approved", "Rejected"]:
            print("Error: Invalid status. Please use 'Approved' or 'Rejected'.")
            return

        leave_request = self.leave_requests[leave_request_id]
        employee_id = leave_request["employee_id"]
        employee = self.employees[employee_id]

        if new_status == "Approved":
            leave_days = leave_request["days"]
            if employee["leave_balance"] >= leave_days:
                employee["leave_balance"] -= leave_days
                leave_request["status"] = "Approved"
                print(f"Leave request {leave_request_id} has been approved.")
            else:
                print("Error: Cannot approve, insufficient leave balance.")
        else:
            leave_request["status"] = "Rejected"
            print(f"Leave request {leave_request_id} has been rejected.")

    def fetch_leave_balance(self, employee_id):
        if employee_id not in self.employees:
            print("Error: Employee not found.")
            return

        balance = self.employees[employee_id]["leave_balance"]
        print(f"Leave balance for Employee ID {employee_id}: {balance} days")

    def display_all_employees(self):
        print("\n--- All Employees ---")
        for emp_id, details in self.employees.items():
            print(f"ID: {emp_id}, Name: {details['name']}, Department: {details['department']}, "
                  f"Joining Date: {details['joining_date']}, Balance: {details['leave_balance']}")

    def display_all_leave_requests(self):
        print("\n--- All Leave Requests ---")
        for req_id, details in self.leave_requests.items():
            print(f"ID: {req_id}, Employee ID: {details['employee_id']}, "
                  f"Start: {details['start_date']}, End: {details['end_date']}, "
                  f"Days: {details['days']}, Status: {details['status']}")

# --- Console Interface ---
def main():
    lms = LeaveManagementSystem()

    # Pre-populate with some data
    lms.add_employee("Prudhvi", "prudhvi@gmail.com", "Engineering", "2025-01-15")
    lms.add_employee("Pavan", "pavan@gmail.com", "HR", "2025-02-20")

    while True:
        print("\n--- Leave Management System ---")
        print("1. Add Employee")
        print("2. Apply for Leave")
        print("3. Approve/Reject Leave")
        print("4. Fetch Leave Balance")
        print("5. Display All Employees")
        print("6. Display All Leave Requests")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter Name: ")
            email = input("Enter Email: ")
            department = input("Enter Department: ")
            joining_date = input("Enter Joining Date (YYYY-MM-DD): ")
            lms.add_employee(name, email, department, joining_date)
        elif choice == "2":
            emp_id = int(input("Enter Employee ID: "))
            start_date = input("Enter Leave Start Date (YYYY-MM-DD): ")
            end_date = input("Enter Leave End Date (YYYY-MM-DD): ")
            lms.apply_for_leave(emp_id, start_date, end_date)
        elif choice == "3":
            req_id = int(input("Enter Leave Request ID: "))
            status = input("Enter Status (Approved/Rejected): ")
            lms.approve_or_reject_leave(req_id, status)
        elif choice == "4":
            emp_id = int(input("Enter Employee ID: "))
            lms.fetch_leave_balance(emp_id)
        elif choice == "5":
            lms.display_all_employees()
        elif choice == "6":
            lms.display_all_leave_requests()
        elif choice == "7":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()