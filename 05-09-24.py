#Write a python program to  add a key to a dictionary ?
my_dict={"a":1,"b":2}
my_dict["c"]=3
print(my_dict)


#Write a python program to check weather the given value is present in the dictionary or not ?
my_dict={"name":"raja","age":20}
value=20
if value in my_dict.values():
    print("the given value is present in the dictionary")
else:
    print("the given value is not present in the dictionary")


"""
Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.
Sample Dictionary
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}""" 
square_dict = {}
for i in range(1, 16):
    square_dict[i] = i**2
print(square_dict)

#Write a python program to create a dictionary from the string ?
s = 'hello world'
d = {}
for char in s:
    if char != ' ':
        if char in d:
            d[char] += 1
        else:
            d[char] = 1
print(d)


#Write a python program to combine two dictionaries by adding values of common keys ?
dict_1={"a":1,"b":2,"c":3}
dict_2={"a":4,"b":5,"c":6}
for key in dict_1 and dict_2:
    dict_1[key]=dict_1[key]+dict_2[key]
print(dict_1)


#Write a python program to merge two python dictionaries ?
dict_1={"name":'ram',"age":25}
dict_2={"city":"nellore","job":"engineer"}
dict_1.update(dict_2)
print(dict_1)


#Write  a python program to sort dictionary by keys or values ?
my_dict = {'c': 8, 'b': 6, 'a': 1, 'd': 2}
sorted_by_keys = sorted(my_dict.items())
print(dict(sorted_by_keys))


#Write a Python program to create a dictionary from a string.  Note: Track the count of the letters from the string.
"""Sample string : 'w3resource'
Expected output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}"""

string = 'w3resource'
char_count = {}
for char in string:
    if char in char_count:
        char_count[char] = char_count[char]+ 1
    else:
        char_count[char] = 1
print(char_count)