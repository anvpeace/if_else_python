"""
8. Loop and Input  

a) Request two numbers, n1 and n2 from the console. 

b) n1 and n2 can be any integer value. 

c) Use a while loop to horizontally print n1 to n2 with increment by 1 if n1 is smaller than n2. 

d) Use a for loop to horizontally print n1 to n2 with decrement by 1 if n1 is greater than n2. 

e) Print a message, “n1 = n2” if n1 is equal to n2. Input text can be any content.  

Just make sure to precisely match the output format below. 

Example Output 1
Enter a number n1: 1
Enter a number n2: 10
1|2|3|4|5|6|7|8|9|10

Example Output 2
Enter a number n1: 11
Enter a number n2: 1
11|10|9|8|7|6|5|4|3|2|1

Example Output 3
Enter a number n1: 10
Enter a number n2: 10
n1 = n2


"""

# Request two numbers, n1 and n2 from the console
n1 = int(input("Enter a number n1: "))
n2 = int(input("Enter a number n2: "))

# Use a while loop to horizontally print n1 to n2 with increment by 1 if n1 is smaller than n2
if n1 < n2:
    i = n1
    while i <= n2:
        print(i, end='|')
        i += 1

# Use a for loop to horizontally print n1 to n2 with decrement by 1 if n1 is greater than n2
elif n1 > n2:
    for i in range(n1, n2 - 1, -1):
        print(i, end='|')

# Print a message, “n1 = n2” if n1 is equal to n2
else:
    print("n1 = n2")