"""
7. Sentinel While Loop 

a) Implement a while loop to request numbers from the console and insert them into a list.  

b) Insert all the numbers into a list. Page 2 of 3 

c) Stop requesting values if the user input is a zero (0). 

d) Print all elements of the list, sum and average.  
Note that 0 should not be added to the list.  Input text can be any content.  
Just make sure to precisely match the output format below. 

Example Output: 
Enter a number or 0 to stop: 1 
Enter a number or 0 to stop: -10 
Enter a number or 0 to stop: 2.34 
Enter a number or 0 to stop: 56.78 
Enter a number or 0 to stop: 123 
Enter a number or 0 to stop: 0
"""

# Initialize an empty list to store numbers
numbers = []

# Initialize variables for sum and count
sum_numbers = 0
count = 0

while True:
    # Request a number from the user
    num = float(input("Enter a number or 0 to stop: "))
    
    # Check if the input is 0, if so, break out of the loop
    if num == 0:
        break
    
    # Append the number to the list if it's not zero
    numbers.append(num)
    
    # Add the number to the sum
    sum_numbers += num
    
    # Increment the count
    count += 1

# Calculate the average
average = sum_numbers / count if count > 0 else 0


print(f"\nSum = {sum_numbers}")
print(f"Average = {average}")
print("Number(s) entered:", end=' ')
for i in range(len(numbers)):
    if i < len(numbers) - 1:
        print(numbers[i], end=' ')
    else:
        print(numbers[i])
        
# userInput = True

# while userInput == True:
#    usrVal = input("Enter a number or 0 to stop: ")

#    vals = list(usrVal)
#    print(vals)

#     if usrVal == "0":
#             userInput = False
#             break
#     print()

