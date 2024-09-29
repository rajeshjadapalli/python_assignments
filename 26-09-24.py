"""
1.Create a class Person that has instance variables name, age, and gender. Add methods to:
Initialize these variables.
Update the age.
Display the person's information.
 Exercise:
 > Create multiple instances of the Person class.
 > Change the age of one person and display the updated information."""
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def update_age(self, new_age):
        self.age = new_age
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}")
person1 = Person("rani", 30, "Female")
person2 = Person("raja", 25, "Male")
person1.display_info()
person2.display_info()
person1.update_age(31)
person1.display_info()
print(".......")


"""
2.Create a class Company that keeps track of the total number of employees using a static variable total_employees. 
  Each employee has instance variables name and department. Every time an employee is added, the total_employees should increment.
  Exercise:
   >Create multiple employee instances.
   >Print the total number of employees after adding each new employee.
   >Check whether changing the total_employees in one instance affects the others."""
  
class Company:
    total_employees = 0  
    def __init__(self, name, department):
        self.name = name
        self.department = department
        Company.total_employees += 1  
employee1 = Company("ramu", "banking")
print(f"Total Employees after adding {employee1.name}: {Company.total_employees}")
employee2 = Company("suresh", "IT")
print(f"Total Employees after adding {employee2.name}: {Company.total_employees}")
employee3 = Company("raja", "hr")
print(f"Total Employees after adding {employee3.name}: {Company.total_employees}")
print(f"final Total Employees: {Company.total_employees}")
employee1.total_employees = 6
print(f"Total Employees after changing in employee1: {Company.total_employees}")
print(f"employee1.total_employees: {employee1.total_employees}")
print(".......")


"""
3.Create a class Rectangle that has instance variables length and width. 
  Add a method calculate_area that  calculates and prints the area of the rectangle using local variables inside the method.
  Exercise:
    >Create instances of the Rectangle class with different lengths and widths.
    >Calculate and print the area for each rectangle."""
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def calculate_area(self):
        area = self.length * self.width 
        print(f"Area of rectangle with length {self.length} and width {self.width} is: {area}")
rectangle1 = Rectangle(3, 6)
rectangle2 = Rectangle(2, 4)
rectangle3 = Rectangle(7, 9)
rectangle1.calculate_area()
rectangle2.calculate_area()
rectangle3.calculate_area()
print(".......")

"""
4.Create a class Employee where:
  Each employee has an instance variable salary.
  There is a static variable bonus shared by all employees. The bonus is applied to each employee's salary.
  Write a method total_salary that calculates the total salary for an employee (including the bonus).
  Exercise:
   >Create several employee instances with different salaries.
   >Change the bonus amount (static variable) and see how it affects all employees.
   >Calculate and print the total salary for each employe"""
class Employee:
    bonus = 0
    def __init__(self, salary):
        self.salary = salary
    def total_salary(self):
        return self.salary + Employee.bonus
employee1 = Employee(10000)
employee2 = Employee(20000)
employee3 = Employee(30000)
print(f"Total salary for Employee 1: {employee1.total_salary()}")
print(f"Total salary for Employee 2: {employee2.total_salary()}")
print(f"Total salary for Employee 3: {employee3.total_salary()}")
Employee.bonus = 5000
print(f"Total salary for Employee 1 after bonus change: {employee1.total_salary()}")
print(f"Total salary for Employee 2 after bonus change: {employee2.total_salary()}")
print(f"Total salary for Employee 3 after bonus change: {employee3.total_salary()}")