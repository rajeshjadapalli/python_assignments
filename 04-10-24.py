#1. Single Inheritance
"""
Problem Statement: Create a base class Animal with an attribute name and a method speak(). Then, create a derived class Dog that inherits from Animal and overrides the speak() method to print "Bark".
 
Tasks:
Define a base class Animal with an __init__ method that takes name as a parameter.
Define a method speak() in Animal that prints "Animal sound".
Create a derived class Dog that inherits from Animal and overrides the speak() method to print "Bark".
Create an instance of Dog and call the speak() method."""
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("Animal sound")
class Dog(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)
    def speak(self):
        print("Bark")
dog=Dog("jimmy")
print(dog.name)
dog.speak()



#2. Multiple Inheritance

"""1.Problem Statement: Create a class Teacher with an attribute subject. Then, create a class Researcher with an attribute field. Finally, create a class TeachingResearcher that inherits from both Teacher and Researcher, and has an additional method to display both attributes.

Tasks:
Define a Teacher class with an __init__ method to initialize subject.
Define a Researcher class with an __init__ method to initialize field.
Define a TeachingResearcher class that inherits from both Teacher and Researcher, and has an __init__ method to initialize both subject and field. Add a method to display both.
Create an object of TeachingResearcher and display its attributes."""
class Teacher:
    def __init__(self, subject):
        self.subject = subject
class Researcher:
    def __init__(self, field):
        self.field = field
class TeachingResearcher(Teacher, Researcher):
    def __init__(self, subject, field):
        Teacher.__init__(self, subject)
        Researcher.__init__(self, field)
    def display_details(self):
        print(f"Subject: {self.subject}")
        print(f"Field: {self.field}")
obj = TeachingResearcher("science", "Ai")
obj.display_details()



"""2.Problem Statement: Create two base classes: Bird and Flyable. Bird should have an attribute species, and Flyable should have a method fly(). Then, create a derived class Eagle that inherits from both Bird and Flyable.

Tasks:
Define a class Bird with an attribute species.
Define a class Flyable with a method fly() that prints "Flying".
Create a class Eagle that inherits from both Bird and Flyable, and has a method to display species and flying capability.
Create an instance of Eagle and call its methods."""
class Bird:
    def __init__(self, species):
        self.species = species
class Flyable:
    def fly(self):
        print("Flying")
class Eagle(Bird, Flyable):
    def display_details(self):
        print(f"Species: {self.species}")
        self.fly()
eagle = Eagle("Eagle")
eagle.display_details()



#3. Multilevel Inheritance
"""
Problem Statement: Create a class hierarchy where Person is the base class, Employee is derived from Person, and Manager is derived from Employee. Each class should add an additional attribute, and a method to display all attributes from the hierarchy.

Tasks:
Define a base class Person with attributes name and age.
Define a derived class Employee with an additional attribute salary.
Define another derived class Manager that inherits from Employee and adds an attribute department.
Implement methods to display the information in each class.
Create an instance of Manager and display its information."""
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display_person(self):
        print(f"name:{self.name},age:{self.age}")
class employee(person):
    def __init__(self,name,age,salary):
        person.__init__(self,name,age)
        self.salary=salary
    def display_employee(self):
        self.display_person()
        print(f"salary:{self.salary}")
class manager(employee):
    def __init__(self,name,age,salary,department):
        employee.__init__(self,name,age,salary)
        self.department=department
    def display_manager(self):
        self.display_employee()
        print(f"department:{self.department}")
manager=manager('raja',20,25000,"software")
print("Manager Information:")
manager.display_manager()



#4. Hierarchical Inheritance

"""1.Problem Statement: Design a class hierarchy for an employee management system with the following structure:

Employee: Base class with name and salary.
Developer: Inherits from Employee with an additional attribute programming_language.
Manager: Inherits from Employee with an additional attribute team_size.
Intern: Inherits from Developer and has an additional attribute internship_duration.
Implement a method to display the details of each employee."""
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def display(self):
        print(f"Name: {self.name}, Salary: {self.salary}")
class Developer(Employee):
    def __init__(self, name, salary, language):
        Employee.__init__(self, name, salary)
        self.language = language
    def display(self):
        Employee.display(self)
        print(f"Language: {self.language}")
class Manager(Employee):
    def __init__(self, name, salary, team_size):
        Employee.__init__(self, name, salary)
        self.team_size = team_size
    def display(self):
        Employee.display(self)
        print(f"Team Size: {self.team_size}")
class Intern(Developer):
    def __init__(self, name, salary, language, duration):
        Developer.__init__(self, name, salary, language)
        self.duration = duration
    def display(self):
        Developer.display(self)
        print(f"Internship Duration: {self.duration} months")
developer = Developer("ram", 20000, "Python")
manager = Manager("kiran", 30000, 10)
intern = Intern("sameer", 40000, "Java", 6)
developer.display()
manager.display()
intern.display()



"""2.Problem Statement: Create a base class Vehicle with attributes brand and model. Then, create two derived classes Car and Bike, both inheriting from Vehicle, and adding their own attributes and methods.

Tasks:
Define a base class Vehicle with attributes brand and model.
Create a derived class Car that inherits from Vehicle and adds an attribute num_doors.
Create another derived class Bike that inherits from Vehicle and adds an attribute type.
Implement methods to display the details of the vehicles.
Create instances of both Car and Bike and display their information."""
class vehicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def display_vehicle(self):
        print(f"brand:{self.brand},model:{self.model}")
class car(vehicle):
    def __init__(self,brand,model,num_doors):
        vehicle.__init__(self,brand,model)
        self.num_doors=num_doors
    def display_car(self):
        self.display_vehicle()
        print(f"num_doors:{self.num_doors}")
class bike(vehicle):
    def __init__(self,brand,model,type):
        vehicle.__init__(self,brand,model)
        self.type=type
    def display_bike(self):
        self.display_vehicle()
        print(f"type:{self.type}")
car=car("toyoto","camry",4)
car.display_car()
bike=bike("honda","cbz","sports")
bike.display_bike()



#5. Hybrid Inheritance
"""
Problem Statement: Create a class structure to represent hybrid inheritance:

Device: Base class with name attribute.
Phone: Derived from Device with an additional phone_number attribute.
Tablet: Derived from Device with an additional screen_size attribute.
Smartphone: Derived from both Phone and Tablet with an additional attribute os.

Tasks:
Define a base class Device with an attribute name.
Define a class Phone that inherits from Device and adds an attribute phone_number.
Define a class Tablet that inherits from Device and adds an attribute screen_size.
Define a class Smartphone that inherits from both Phone and Tablet, adding an attribute os.
Implement methods to display all attributes of the Smartphone.
Create an instance of Smartphone and display its information.
nce:"""
class Device:
    def __init__(self, name):
        self.name = name
    def display_device(self):
        print(f"Name: {self.name}")
class Phone(Device):
    def __init__(self, name, phone_number):
        Device.__init__(self, name)
        self.phone_number = phone_number
    def display_phone(self):
        self.display_device()
        print(f"Phone Number: {self.phone_number}")
class Tablet(Device):
    def __init__(self, name, screen_size):
        Device.__init__(self, name)
        self.screen_size = screen_size
    def display_tablet(self):
        self.display_device()
        print(f"Screen Size: {self.screen_size} inches")
class Smartphone(Phone, Tablet):
    def __init__(self, name, phone_number, screen_size, os):
        Phone.__init__(self, name, phone_number)
        Tablet.__init__(self, name, screen_size)
        self.os = os
    def display_smartphone(self):
        self.display_phone()
        print(f"Screen Size: {self.screen_size} inches")
        print(f"Operating System: {self.os}")
smartphone = Smartphone("iPhone", "1234567890", 6.1, "iOS")
print("Smartphone Details:")
smartphone.display_smartphone()



#6.Basic Inheritance
"""
Problem Statement: Create a class Person with attributes: name and age. Create another class Student that inherits from Person and has an additional attribute grade. Define methods in both classes to display the attributes.

Tasks:
Define a Person class with an __init__ method to initialize name and age.
Define a Student class that inherits from Person, with an additional attribute grade.
Define a display_info method in both Person and Student classes to print all attributes.
Create objects for both Person and Student and display their information."""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
class Student(Person):
    def __init__(self, name, age, grade):
        Person.__init__(self, name, age)
        self.grade = grade
    def display_info(self):
        Person.display_info(self)
        print(f"Grade: {self.grade}")
person = Person("ramesh", 20)
print("Person Information:")
person.display_info()
student = Student("suresh", 30, "A")
print("\nStudent Information:")
student.display_info()
