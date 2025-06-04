"""
9. Loop and Input 

a) Request the lower bound, lower and the upper bound, upper from the console. 

b) Request an increment value incVal from the console. 

c) Use a while loop to increment from lower to upper by increments of incVal (see example output below).   

For example, with increment of 3, the program will output 0 3 6 9 12, given lower of 0 and upper of 12. 

d) Use a while loop to vertically print all values in between each increment. 

e) Use a for loop to vertically print all values in between each increment. 

Input text can be any content.  
Just make sure to precisely match the output format below. 

USING WHILE LOOP
Enter the lower bound: 5
Enter the upper bound: 15
Enter a number to increment by: 5

5
10
15

USING FOR LOOP
Enter the lower bound: 5
Enter the upper bound: 55
Enter a number to increment by: 10

5
15
25
35
45
55
"""

# Using while loop
print("USING WHILE LOOP")
lower = int(input("Enter the lower bound: "))
upper = int(input("Enter the upper bound: "))
incVal = int(input("Enter a number to increment by: "))

current = lower
while current <= upper:
    print(current)
    current += incVal

print()

# Using for loop
print("USING FOR LOOP")
lower = int(input("Enter the lower bound: "))
upper = int(input("Enter the upper bound: "))
incVal = int(input("Enter a number to increment by: "))