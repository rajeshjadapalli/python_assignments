"""
#python key words_words which are reserved for special meaning
help("keywords")
import keyword
print(keyword.kwlist)

#type conversion_Converting the value of one data type to another data type is called Type Conversion or Type Casting.
#Adding Two Numbers
x = int(input("enter x number : "))
y = int(input("enter y number : "))
print(x+y)
"""

#operators
"""
Arithmetic Operators
Comparison Operators
Assignment Operators
Logical Operators
Bitwise Operators
Identity Operators
Membership Operators
Conditional Expressions
"""
"""
arthimetical operators
Addition:"+"
Subtraction:"-"
Multiplication:"*"
Modulus:"%"
Exponentiation:"**"
division:"/"
floor division:"//"


#addition:"+"
a = int(input("enter a number : "))#5
b = int(input("enter b number : "))#10
result=(a+b)#15
print(result)
"""

#Exponentiation:"**"
"""
a = int(input("enter a number : "))#2
b = int(input("enter b number : "))#3
print(a**b)#16
"""

#logical operators: and,or,not:-The logical operators are used to perform logical operations on Boolean values.
#Gives True or False as the result.  
"""
#and
a = input("enter a number : ")#true
b = input("enter b number : ")#false
result=a and b
print(result)#false

#or
a = input("enter a number : ")#true
b = input("enter b number : ")#false
result=a or b
print(result)#true

#not
a = input("enter a number : ")#true
result=not a
print(result)#false
"""
#Relational operators :in Python are used to compare values and return a boolean result (True or False). Here are the relational operators with examples:
"""
Equal to (==)
Not equal to (!=)
Greater than (>)
Less than (<)
Greater than or equal to (>=)
Less than or equal to (<=)
"""
"""
#Equal to (==)
a=int(input("enter a number : "))#5
b=int(input("enter b number : "))#5
print(a==b)#true
"""
"""
#Greater than or equal to (>=)
a=int(input("enter a number : "))#10
b=int(input("enter b number : "))#20
print(a>=b)#false
"""
#Assignment Operator (=)
"""
Addition Assignment Operator (+=)
Subtraction Assignment Operator (-=)
Multiplication Assignment Operator (*=)
Division Assignment Operator (/=)
Floor Division Assignment Operator (//=)
Modulus Assignment Operator (%=)
Exponentiation Assignment Operator (**=)
Bitwise AND Assignment Operator (&=)
Bitwise OR Assignment Operator (|=)
Bitwise XOR Assignment Operator (^=)
Bitwise Left Shift Assignment Operator (<<=)
Bitwise Right Shift Assignment Operator (>>=)
"""
#Floor Division Assignment Operator (//=)
a = 17
b = 4
result = a // b   #4
print(result)
#Bitwise operators: in Python allow you to perform operations on the binary representations of integers
"""
Here’s a list of the bitwise operators in Python, 

1. **Bitwise AND (`&`)**: Compares each bit of two numbers. If both bits are `1`, the resulting bit is `1`; otherwise, it's `0`.

2. **Bitwise OR (`|`)**: Compares each bit of two numbers. If at least one of the bits is `1`, the resulting bit is `1`; otherwise, it's `0`.

3. **Bitwise XOR (`^`)**: Compares each bit of two numbers. If the bits are different, the resulting bit is `1`; if they are the same, the resulting bit is `0`.

4. **Bitwise NOT (`~`)**: Inverts all the bits of a number, changing `0` to `1` and `1` to `0`. This is also known as the bitwise complement.

5. **Bitwise Left Shift (`<<`)**: Shifts the bits of a number to the left by a specified number of positions, effectively multiplying the number by `2` for each shift.

6. **Bitwise Right Shift (`>>`)**: Shifts the bits of a number to the right by a specified number of positions, effectively dividing the number by `2` for each shift.
"""
#Bitwise AND (&)
a = 5  # In binary: 0101
b = 3  # In binary: 0011
result = a & b
print(result)  # Output will be 1 (In binary: 0001)
#uni code values or ascii values
"""
Unicode Ranges
48 - 57 -> Number Digits (0 - 9)
65 - 90 -> Capital Letters (A - Z)
97 - 122 -> Small Letters (a - z)
Rest -> Special Characters, Other Languages
"""


print("A"<"B")# (65<66)=TRUE
print(ord("A"))#65
print(ord("B"))#66

print(chr(100))#returns integer value to character "d"


#Identity Operators
"""
Identity operators are used to compare the memory locations of two objects. They check whether two variables point to the same object in memory.

is: Returns True if both variables point to the same object.
is not: Returns True if both variables do not point to the same object
"""
a = [1, 2, 3]
b = a             # b points to the same object as a
c = [1, 2, 3]  # c is a different object with the same content
print(a is b)       # True: a and b point to the same object
print(a is c)       # False: a and c are different objects
print(a is not c)   # True: a and c are different objects

#Membership Operators
"""
Membership operators are used to check if a value is a member of a collection (such as a list, tuple, or string).

in: Returns True if the value is found in the collection.
not in: Returns True if the value is not found in the collection.
"""

numbers = [1, 2, 3, 4, 5]
text = "Hello, World!"
print(3 in numbers)      # True: 3 is in the list numbers
print(6 in numbers)      # False: 6 is not in the list numbers
print('Hello' in text)  # True: 'Hello' is a substring of text
print('hello' in text)  # False: 'hello' is not a substring of text 
