"""1.Given a tuple containing nested tuples, write a Python program to flatten it into a single tuple.
Example Tuple: (1, (2, 3), (4, 5, 6)) # Expected Output: (1, 2, 3, 4, 5, 6)"""
def flatten_tuple(nested_tuple):
    result = []
    for item in nested_tuple:
        if type(item) == tuple:
            result.extend(flatten_tuple(item)) 
        else:
            result.append(item)
    return tuple(result)
example_tuple = (1, (2, 3), (4, 5, 6))
flattened_tuple = flatten_tuple(example_tuple)
print(flattened_tuple)

 
"""2.Write a Python program to sort a tuple of tuples based on the second element
of each tuple.
Example Tuple: ((1, 2), (3, 1), (5, 0))Expected Output: ((5, 0), (3, 1), (1, 2))"""
tuples = ((1,2), (5,0), (3,1))
tuples_list = list(tuples)
tuples_list.sort()
sorted_tuples =tuple(tuples_list)
print(sorted_tuples)