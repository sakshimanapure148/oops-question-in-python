# Question 13: Employee Salary
# Create an Employee class with employee name and monthly salary.
# Calculate and display the annual salary using a method.

class Employee:
    def __init__(self, employee_name, monthly_salary):
        self.employee_name = employee_name
        self.monthly_salary = monthly_salary

    def calculate_annual_salary(self):
        return self.monthly_salary * 12

    def display_details(self):
        print("Employee Name:", self.employee_name)
        print("Monthly Salary:", self.monthly_salary)
        print("Annual Salary:", self.calculate_annual_salary())


# Create an object
employee1 = Employee("Aarav", 25000)

# Display employee details
employee1.display_details()
