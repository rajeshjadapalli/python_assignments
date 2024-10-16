"""1.Create a class Vehicle with attributes brand and year. The class should have a method get_info() that returns the brand and year of the vehicle. Then, create two subclasses:

Car, which adds an attribute number_of_doors.
Motorcycle, which adds an attribute has_sidecar.
Both subclasses should override the get_info() method to include their respective additional attributes in the returned string.
"""
class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
    def get_info(self):
        print(f"Brand: {self.brand}, Year: {self.year}")
class Car(Vehicle):
    def __init__(self, brand, year, doors):
        Vehicle.__init__(self, brand, year)
        self.doors = doors
    def get_info(self):
        Vehicle.get_info(self)
        print(f"Doors: {self.doors}")
class Motorcycle(Vehicle):
    def __init__(self, brand, year, sidecar):
        Vehicle.__init__(self, brand, year)
        self.sidecar = sidecar
    def get_info(self):
        Vehicle.get_info(self)
        print(f"Sidecar: {self.sidecar}")
car = Car("Toyota", 2020, 4)
motorcycle = Motorcycle("Honda", 2015, True)
print("Car Details:")
car.get_info()
print("\nMotorcycle Details:")
motorcycle.get_info()


"""
2.Define an abstract class Animal with an abstract method make_sound(). Then, create three classes that inherit from Animal:

Dog with the sound "Woof".
Cat with the sound "Meow".
Cow with the sound "Moo".
Create a function play_sound(animal) that takes an object of type Animal and calls its make_sound() method.
"""
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        None
class Dog(Animal):
    def make_sound(self):
        print("dog: Woof")
class Cat(Animal):
    def make_sound(self):
        print("cat: Meow")
class Cow(Animal):
    def make_sound(self):
        print("cow: Moo")
def play_sound(animal):
    animal.make_sound()
dog = Dog()
cat = Cat()
cow = Cow()
print("Animal Sounds:")
play_sound(dog)
play_sound(cat)
play_sound(cow)


"""
3.Create an abstract class BankAccount with methods deposit(), withdraw(), and get_balance(). Then, create two subclasses:

SavingsAccount, where the withdraw() method ensures that the balance cannot go below $500.
CurrentAccount, where the withdraw() method allows the balance to go negative (up to $1000 overdraft).
Ensure that only deposit() and withdraw() are exposed to the user, and the balance is encapsulated (hidden).
"""
from abc import ABC, abstractmethod
class BankAccount(ABC):
    def __init__(self, balance=0):
        self._balance = balance 
    @abstractmethod
    def deposit(self, amount):
        pass
    @abstractmethod
    def withdraw(self, amount):
        pass
class SavingsAccount(BankAccount):
    def deposit(self, amount):
        self._balance += amount
    def withdraw(self, amount):
        if self._balance - amount >= 500:
            self._balance -= amount
        else:
            print("Insufficient funds. Minimum balance: $500.")
class CurrentAccount(BankAccount):
    def __init__(self, balance=0):
        super().__init__(balance)
        self._overdraft_limit = -1000
    def deposit(self, amount):
        self._balance += amount
    def withdraw(self, amount):
        if self._balance - amount >= self._overdraft_limit:
            self._balance -= amount
        else:
            print("Overdraft limit exceeded.")
savings_account = SavingsAccount(1000)
current_account = CurrentAccount(500)
savings_account.deposit(200)
savings_account.withdraw(800)
savings_account.withdraw(200)
current_account.deposit(500)
current_account.withdraw(1200)
current_account.withdraw(500)



"""
4.Create a base class Employee with attributes name and salary, and methods get_details() and get_salary(). Then create two subclasses:

Manager, which adds an attribute department.
Developer, which adds an attribute programming_language.
Both subclasses should override the get_details() method to include their respective additional attributes in the returned string.

Add a method increase_salary(percent) in the Employee class that increases the salary by a given percentage.
"""
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def get_details(self):
        return f"name: {self.name},salary: {self.salary}"
    def get_salary(self):
        return f"salary: {self.salary}"
    def increase_salary(self,percent):
        self.salary+=self.salary*(percent/100)
        print(f"{self.name} salary increase by {percent}% new salary was: {self.salary}")
class Manager(Employee):
    def __init__(self,name,salary,department):
        super().__init__(name,salary)
        self.department=department
    def get_details(self):
        return f"name: {self.name},salary: {self.salary},department: {self.department}"

class Developer(Employee):
    def __init__(self,name,salary,programming_language):
        super().__init__(name,salary)
        self.programming_language=programming_language
    def get_details(self):
        return f"name: {self.name},salary: {self.salary},programming_language: {self.programming_language}"
emp1=Manager("ram",20000,"Hr")
emp2=Developer("raja",30000,"python")
print(emp1.get_details())
print(emp2.get_details())
emp1.increase_salary(10)
emp2.increase_salary(15)



"""
5.Create an abstract class Media with an abstract method play(). Then create the following subclasses:

Audio, which plays a .mp3 file.
Video, which plays a .mp4 file.
LiveStream, which plays a live stream.
Implement a function start_media(media) that takes an object of type Media and calls its play() method. Demonstrate polymorphism by passing different types of media to this function.
"""
from abc import ABC,abstractmethod
class Media(ABC):
    @abstractmethod
    def play(self):
        pass
class Audio(Media):
    def __init__(self,file):
        self.file=file
    def play(self):
        print(f"playing {self.file}.mp3")
class Video(Media):
    def __init__(self,file):
        self.file=file
    def play(self):
        print(f"playing {self.file}.mp4")
class Livestream(Media):
    def __init__(self,file):
        self.file=file
    def play(self):
        print(f"playing livestream {self.file}")
def play(media): 
    media.play()
audio=Audio("songs")
video=Video("movie")
livestream=Livestream("link")
play(audio)
play(video)
play(livestream)


"""
6.Create an abstract class LibraryItem with abstract methods borrow() and return_item(). Then create two subclasses:

Book, with attributes title, author, and num_copies.
DVD, with attributes title, director, and duration.
Implement a function borrow_item(item) that borrows the library item and decreases the number of available copies (for books) or marks the DVD as borrowed.
"""
from abc import ABC, abstractmethod
class LibraryItem(ABC):
    @abstractmethod
    def borrow(self):
        pass
    @abstractmethod
    def return_item(self):
        pass
class Book(LibraryItem):
    def __init__(self, title, author, num_copies):
        self.title = title
        self.author = author
        self.num_copies = num_copies
    def borrow(self):
        if self.num_copies > 0:
            self.num_copies -= 1
            print(f"Borrowed '{self.title}'. Copies left: {self.num_copies}")
        else:
            print(f"No more '{self.title}' copies available.")
    def return_item(self):
        self.num_copies += 1
        print(f"Returned '{self.title}'. Copies now: {self.num_copies}")
class DVD(LibraryItem):
    def __init__(self, title, director, duration):
        self.title = title
        self.director = director
        self.duration = duration
        self.is_borrowed = False
    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"Borrowed DVD '{self.title}' by {self.director}.")
        else:
            print(f"DVD '{self.title}' is already borrowed.")
    def return_item(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(f"Returned DVD '{self.title}'.")
        else:
            print(f"DVD '{self.title}' was not borrowed.")
def borrow_item(item):
    item.borrow()
book = Book("money", "George", 3)
dvd = DVD("Inception", "naveen", "2h")
borrow_item(book)
borrow_item(dvd)
book.return_item()
dvd.return_item()