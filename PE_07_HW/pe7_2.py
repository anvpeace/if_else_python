"""
 For & While 
 a) Use a for loop to print all the numbers are even and multiples of 3 from 1 to 1000 inclusive. 
 
 b) Convert the for loop to a while loop. 
 
 Example Output 6 12 18 24 30 36 42 48 54 60 66 … 996 
"""

# for num in range(1, 1001, 2):
#     if num % 2 == 0:
#         print(num)
# squares = [value**2 for value in range(1, 11)] .. similar concept

num = [value for value in range(1, 1001)]
for p in num:
    if p % 2 == 0 and p % 3 == 0:
 
       print(p)

print("`````````````````````````````````````````````````````````````\n")

x = 1
while x <= 1000:
    x +=1
    if x % 2 == 0 and x % 3 == 0:
        print(x)
