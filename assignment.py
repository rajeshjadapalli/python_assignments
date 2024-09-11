"""1.Write a program which will find all such numbers which are divisible by 7 but are not a 
multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be 
printed in a comma-separated sequence on a single line."""
start = 2000
end = 3200
seq = []
for num in range(start, end + 1):
    if num % 7 == 0 and num % 5 != 0:
        seq.append(str(num)) 
result = ','.join(seq)
print(result)


"""2.With a given integral number n, write a program to generate a dictionary that contains (i, 
i*i) such that is an integral number between 1 and n (both included). and then the program 
should print the dictionary. Suppose the following input is supplied to the program: 8 Then, 
the output should be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}"""
n= 8
d= {}
for i in range(1, n+1):
    d[i] = i*i
print(d)


"""3.Write a program which accepts a sequence of comma-separated numbers from console 
and generate a list and a tuple which contains every number. Suppose the following input 
is supplied to the program: 34,67,55,33,12,98 Then, the output should be: ['34', '67', '55', 
'33', '12', '98'] ('34', '67', '55', '33', '12', '98')"""
numbers = input("Enter numbers: ")
num_list = numbers.split(',')
num_tuple = tuple(num_list)
print(num_list)
print(num_tuple) 


"""4.Write a program that accepts a comma separated sequence of words as input and prints 
the words ina comma-separated sequence after sorting them alphabetically. Suppose the 
following input is supplied to the program: without, hello, bag, world Then, the output 
should be: bag,hello,without,world"""
words = input("Enter comma-separated words: ")
word_list = sorted(words.split(','))
sorted_words = ','.join(word_list)
print(sorted_words)