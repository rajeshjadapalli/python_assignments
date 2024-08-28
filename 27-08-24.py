 #string :-string is a sequence of characters b/w single and double quotes
"""
example
name="krishna"
"12345"
"some@example.com"
"""

#Working with Strings
#String Concatenation
a = "Hello" + " " + "World"
print(a) #Hello World


#Concatenation Errors:-String Concatenation is possible only with strings.
"""
a = "*" + 10
print(a)#wrong way
"""

#String Repetition:-operator is used for repeating strings any number of times as required.
a = "*" * 10
print(a)#**********
s = "Python"
s = ("* " * 3) + s + (" *" * 3)
print(s)#* * * Python * * *


#Length of String:-len() returns the number of characters in a given string.
username = "ramesh"
length = len(username)
print(length)#6


#String Indexing:-We can access an individual character in a string using their positions (which start from 0) .These positions are also called as index.
username = "Ravi"
first_letter = username[0]
print(first_letter)#R


#IndexError:-Attempting to use an index that is too large will result in an error:
"""
username = "Raja"
print(username[4])#wrong way-IndexError: string index out of range
"""

#Negative Indexing:-Using a negative index returns the nth item from the end of list.Last item in the list can be accessed with index
list_a = [5, 4, 3, 2, 1]
item = list_a[-4]
print(item)#4


#Extended Slicing and String Methods-step index
a = "Waterfall"
part = a[1:6:2]
print(part)#aef


#String Slicing:-Obtaining a part of a string is called string slicing.
message = "Hi Ravi"
part = message[3:7]
print(part)#Ravi


#Slicing to End:-If end index is not specified, slicing stops at the end of the string.
message = "Hi Ravi"
part = message[3:]
print(part)#Ravi


#Slicing from Start:-If start index is not specified, slicing starts from the index 0.
message = "Hi Ravi"
part = message[:2]
print(part)#Hi

#Methods:-Python has a set of built-in reusable utilities.
#String Methods
"""
isdigit()
strip()
lower()
upper()
startswith()
endswith()
replace()
"""

#string methods
#strip()-Removes all the leading and trailing spaces from a string.
#lstrip()-removes left side spaces
#rstrip()-removes right side spaces
mobile = "   98765433210    "
mobile = mobile.rstrip()
print(mobile)

#Strip - Specific characters
name = "Ravi......"
name = name.strip(".")
print(name)#Ravi

#split()-Splits a string into a list at every specified separator.If no separator is specified, default separator is whitespace.
nums = "1 2 3 4 "
num_list = nums.split()
print(num_list)#['1', '2', '3', '4']

#String as Separator
string_a = "Python is a programming language"
list_a = string_a.split("a")
print(list_a)#['Python is ', ' progr', 'mming l', 'ngu', 'ge']

#count()-Returns the number of elements with the specified value.
list_a = [1, 2, 3, 4, 5, 6]
count = list_a.count(2)
print(count)#1

#index()-Returns the index at the first occurrence of the specified value.
list_a = [1, 3, 2, 3]
index =list_a.index(3)
print(index)#1

#find()
text = "Hello, Python programming!"
index = text.find('Python')
print(index)#7

#rfind()
text = "Hello, Python programming! Python"
index = text.rfind('Python')
print(index)#27