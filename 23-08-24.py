#control statements four types
""""
1. Conditional Statements
   - `if`
   - `else`
   - `elif`

2. Looping (Iteration) Statements
   - `for`
   - `while`

3. Control Flow Alteration Statements or Jump Statements.or transfer statements.
   - `break`
   - `continue`
   - `pass`
   - `return`

 4. Exception Handling Statements or Error Handling statements.
   - `try`
   - `except`
   - `finally`
   - `raise`
"""


#conditional statements

balance = int(input("Balance amount is: "))

if (balance <= 500) and (balance >= 10):
    print("Balance is between 10 and 500")
elif (balance > 500) and (balance <= 1000):
    print("Balance is between 501 and 1000")
elif balance > 1000:
    print("Balance is above 1000")
else:
    print("Balance is below 10")


#Looping (Iteration) Statements
number=10
for i in range(1,number+1):
   print(i)
name="raja"
for char in name:
   print(char)

number=1
while number<=5:
   number=number+1
   print(number)


# break:-break is used to exit a loop when a condition is satisfied.
for i in range(5):
   if i == 3:
     break
   print(i)


#continue:it skips the current itteration and moves to next itteration.
for i in range(5):
   if i == 3:
     continue
   print(i)


#Pass :-pass statement is used as a syntactic placeholder. When it is executed, nothing happens.

number = int(input("number : "))

if number >= 10:
   pass
else:
   print("number is less than 10")
