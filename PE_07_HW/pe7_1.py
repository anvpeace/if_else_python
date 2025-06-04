"""
 Request an integer input, and then print whether the number is a multiple of 10 or not. 
 
 Example 
 Output 1 
 Enter an integer number, and I'll tell you if it's a multiple of ten: 15 15 is not multiple of ten. 
 
 Example Output 2 Enter an integer number, and I'll tell you if it's a multiple of ten: 50 50 is a multiple of ten. 
"""

numberChoice = int(input("Enter an integer number, and I'll tell you if it's a multiple of ten: "))

if numberChoice % 10 == 0:
    print(numberChoice)
    print(f"{numberChoice} is a multiple of 10")
else:
    print(numberChoice)
    print(f"{numberChoice} is not a multiple of 10")