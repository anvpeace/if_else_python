"""
3. Loop & Calculation 

a) Use a for loop to calculate and print the sum of all numbers between 1 to 100 inclusive. 

Example Output Sum = 5050 

b) Use a while loop to calculate and print the sum of all even numbers between 1 to 100 inclusive. 

Example Output Sum = 2550  
"""
sum = 0

for num in range(1, 101):
    sum += num

print(f"Sum: {sum}")


evenNum_Sum = 0

num2 = 2

while num2 <= 100:
    evenNum_Sum += num2
    num2 += 2
print(f"Sum: {evenNum_Sum}")

# while j <= 100:
#     j+=j
#     print(j)