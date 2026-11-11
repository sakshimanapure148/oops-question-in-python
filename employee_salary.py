"""Practice: calculate an employee's annual salary."""

import math


class Employee:
    """Store employee details and calculate yearly salary."""

    def __init__(self, employee_name, monthly_salary):
        if not isinstance(employee_name, str) or not employee_name.strip():
            raise ValueError("Employee name cannot be empty.")
        if (
            isinstance(monthly_salary, bool)
            or not isinstance(monthly_salary, (int, float))
            or not math.isfinite(monthly_salary)
            or monthly_salary < 0
        ):
            raise ValueError("Monthly salary must be a non-negative number.")

        self.employee_name = employee_name.strip()
        self.monthly_salary = monthly_salary

    def calculate_annual_salary(self):
        return self.monthly_salary * 12

    def display_details(self):
        print(f"Employee Name: {self.employee_name}")
        print(f"Monthly Salary: Rs. {self.monthly_salary:,.2f}")
        print(f"Annual Salary: Rs. {self.calculate_annual_salary():,.2f}")


if __name__ == "__main__":
    employee1 = Employee("Aarav", 25000)
    employee1.display_details()
