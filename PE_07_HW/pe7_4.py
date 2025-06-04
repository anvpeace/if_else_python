"""
4. Use a loop to print all the numbers are odd and multiples of 5 from 1 to n inclusive. 

a) n is a user input. 
b) Implement (an if-else) statements to validate n. 

Input text can be any content.  

Just make sure to precisely match the output format below. 
Example Output 1    Enter a positive number: 65  Range = 1 to 65    5 15 25 35 45 55 65   Example Output 2 Enter a positive number: 0 Range = 1 to 0 Invalid input. 

"""
n = int(input("Enter a positive number: "))

for p in range(1, n+1):
    if p % 5 == 0:
        print(p)
else:
        print("Invalid input")
print()