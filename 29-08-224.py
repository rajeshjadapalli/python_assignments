#Python Program to count occurrence of a given characters in string.
name=input("name is : ")
count=0
for i in name:
    count=count+1
print(count)


#Python Program to check if two Strings are Anagram.
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
if sorted(str1) == sorted(str2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")


#Python program to check a String is palindrome or not.
a=input("input is : ")
reverse=a[::-1]
if a==reverse:
    print("is palindrome")
else:
    print("is not palindrome")


#Python program to replace the string space with a given character.
word=input("word is : ")
result=word.replace(" ","@")
print(result) 


#Python program to convert lowercase char to uppercase of string.
char=input("char is :")
result=char.upper()
print(result)


#Python program to convert lowercase vowel to uppercase in string.
input= input("Enter a string: ")
vowels = 'aeiou'
new= ""
for char in input:
    if char in vowels:
        new += char.upper()
    else:
        new+= char
print(new)


#Python program to separate characters in a given string.
name=input("name is :")
result=""
for char in name:
    result=result+char+" "
print(result)


#Python program to remove blank space from string.
name=input("name is :")
result=name.replace(" ","")
print(result)


#Python program to concatenate two strings using join() method.
str_1=input("str_1 is : ")
str_2=input("str_2 is : ")
result="".join([str_1,str_2])
print(result)


#Python program to concatenate two strings without using join() method.
str_1=input("str_1 is : ")
str_2=input("str_2 is : ")
result=str_1+str_2
print(result)


#Python program to remove repeated character from string.
input= input("input is : ")
output= ""
for char in input:
    if char not in output:
        output += char
print(output)
 

#Python program to check given character is vowel or consonant.
char =input("char is : ")
if char.lower() in 'aeiou':
    print("char is a vowel.")
elif char.isalpha():
    print("char is a consonant.")
else:
    print("Invalid input. Please enter a letter.")


#Python program to check given character is digit or not.
char=input("char is : ")
result=char.isdigit()
if result==True:
    print("is_digit")
else:
    print("is not a digit")


#Python program to delete vowels in a given string.
name=input("name is : ")
vowels="aeiouAEIOU"
matter=" "
for char in name:
    if char in vowels:
        continue
    else:
        matter=matter+char
print(matter)


#Python program to count the Occurrence Of Vowels & Consonants in a String.
input_string = input("Enter a string: ")
vowels = 'aeiou'
vowel_count = 0
consonant_count = 0
for char in input_string:
    if char.lower() in vowels:
        vowel_count += 1
    elif char.isalpha():
        consonant_count += 1
print("Vowel count: ", vowel_count)
print("Consonant count:", consonant_count)

#Python program to print the highest frequency character in a String.
input= input("Enter a string: ")
max_count = 0
highest= ''
for char in input:
    count = input.count(char)
    if count > max_count:
        max_count = count
        highest = char
    elif count == max_count:
        continue
print("The highest frequency character is:", highest)


#Python program to Replace First Occurrence Of Vowel With ‘-‘ in String.
input_string = input("Enter a string: ")
vowels = 'aeiouAEIOU'
for char in input_string:
    if char in vowels:
        input_string = input_string.replace(char, '-')
        break
print("Modified string: ", input_string)

#Python program to count alphabets, digits and special characters.
input_string = input("Enter a string: ")
alphabets = 0
digits = 0
special_chars = 0
for char in input_string:
    if char.isalpha():
        alphabets += 1
    elif char.isdigit():
        digits += 1
    else:
        special_chars += 1
print("Alphabets: ", alphabets)
print("Digits: ", digits)
print("Special Characters: ", special_chars)

#Python program to check given character is digit or not using isdigit() method.
name=input("name is : ")
if name.isdigit():
    print("is_digit")
else:
    print("its not a digit")


#Python program to calculate sum of integers in string.
input_string = input("Enter a string: ")
sum_of_integers = 0
for char in input_string:
    if char.isdigit():
        sum_of_integers += int(char)
print(sum_of_integers)


#Python program to print all non repeating character in string.
input=input('input is ;')
output= ""
for char in input:
    if char not in output:
        output += char
print(output)


#Python program to copy one string to another string.
orginal=input("enter the string :")
copied=""
for i in orginal:
    copied+=i
print(orginal)
print(copied)


#Python program to check given character is vowel or consonant.
word=input("word is : ")
vowels="AEIOUaeiou"
if word in vowels:
    print("given character is vowel")
else:
    print("given character is consonant")


#Python program to check given character is digit or not.
name=input("name is : ")
if name.isdigit():
    print("is_digit")
else:
    print("its not a digit")

