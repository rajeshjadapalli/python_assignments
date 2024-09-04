#How do you create a empty tuple on python ?
empty_tuple = ()
print(type(empty_tuple))  # Output: <class 'tuple'>
print(empty_tuple)        # Output: () 


#Write a python program to unpack a tuple into several variables ?
my_tuple = ("John", 30, "New York")
name, age, city = my_tuple
print("Name:", name)
print("Age:", age)
print("City:", city)


#write a python program to add an item to the tuple ? 
my_tuple = ("John", 30, "New York")
my_list = list(my_tuple)
my_list.append("USA")
my_tuple = tuple(my_list)
print(my_tuple)


#Write a python proram to convert tuple into a string ?
my_tuple = ("Hello", "world", "Python")
my_string = ' '.join(my_tuple)
print(my_string)


#Write a python program to find most frequent element in tuple ?  
words = (6, 7, 8, 6, 7, 10)
count = 0
index = words[0]
for i in words:
    curr_freq =words.count(i)
    if(curr_freq > count):
        count = curr_freq
        index = i
print("Maximum element frequency tuple : " + str(index))