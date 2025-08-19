# Leave-Management-System

A simple console-based application to manage employee leaves for a startup.

## Setup and Installation

1.  **Prerequisites:**
    *   Python 3.x

2.  **Running the Application:**
    *   Save the code as `leave_management_system.py`.
    *   Run the following command in your terminal:
        ```bash
        python leave_management_system.py
        ```

## Assumptions

*   Each new employee is credited with an initial leave balance of 20 days.
*   The system only handles full-day leave requests.
*   Weekends and public holidays are counted as leave days.

## Edge Cases Handled

*   **Employee Not Found:** The system checks for the existence of an employee before processing any leave-related action.
*   **Leave Before Joining Date:** Prevents employees from applying for leave before their official start date.
*   **Insufficient Leave Balance:** An employee cannot apply for more leave days than they have available.
*   **Overlapping Leave Requests:** The system prevents an employee from submitting a leave request that overlaps with another pending or approved request.
*   **Invalid Dates:** The end date of a leave request cannot be before the start date.
