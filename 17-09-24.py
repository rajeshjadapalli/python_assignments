#Create a dictionary where the keys are tuples representing coordinates (x, y) and the values are city names. Write a Python program to print the city name for a given coordinate. Example Dictionary: #{(40.7128, -74.0060): "New York", (34.0522, -118.2437): "Los Angeles"} # Input: (40.7128, -74.0060) # Expected Output: "New York"
a={(40.7128, -74.0060): "New York", (34.0522, -118.2437): "Los Angeles"}
input=(34.0522, -118.2437)
if input in a:
    print(a[input])


#Write a Python program to sort a tuple of tuples based on the second element of each tuple. python # Example Tuple: ((1, 2), (3, 1), (5, 0)) # Expected Output: ((5, 0), (3, 1), (1, 2))
def sort_tuple(tup):
    return tuple(sorted(tup, key=lambda x: x[1]))

tup = ((1, 2), (3, 1), (5, 0))
print(sort_tuple(tup))


#Write a Python program to find the minimum and maximum elements in a tuple of integers. python # Example Tuple: (10, 20, 5, 40, 25) # Expected Output: Min: 5, Max: 40
a=(10, 20, 5, 40, 25)
min_value=str(min(a))+(" ,")
max_value=max(a)
print("min:",min_value,"max:",max_value)


#Given a tuple containing nested tuples, write a Python program to flatten it into a single tuple. python # Example Tuple: (1, (2, 3), (4, 5, 6)) # Expected Output: (1, 2, 3, 4, 5, 6)
nested_tuple = (1, (2, 3), (4, 5, 6))
list=[]
for each_char in nested_tuple:
    length=len(str(each_char))
    if length==1:
        list+=[length]
    else:
        for char in each_char:
            list+=[char]
tuple_convert=tuple(list)        
print(tuple_convert)