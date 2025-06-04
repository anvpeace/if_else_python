"""
5. While & For 
a) Implement a while loop to print all the numbers from 9 to 1 inclusive. 

b) Then display Happy New Year! 

c) Convert the while loop to a for loop Example Output 9 8 7 6 5 4 3 2 1 Happy New Year! 

"""
count = 10

while count > 1:
    count -= 1
    print(count)
print("Happy New Year!")

for x in range(10, 1, -1):
    x = x - 1
    print(x)
print("Happy New Year!")

