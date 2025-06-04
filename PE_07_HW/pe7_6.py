"""
6. While & Lists 
a) Request an integer input for the numbers of grades in the list. 
b) Use a loop to generate random grades (1 – 100) in the list, grades. 
c) Request a user input for the passing grade. 
d) Use a loop to store all the passing grades into a new list, passGrades. 
e) Print all the lists. 
Example Output 
 Enter the number of grades in the list: 10 
 Enter the passing grade: 65 
 Updated List: [70, 81, 66, 94, 65] 
 Original List: [22, 17, 70, 81, 35, 33, 66, 24, 94, 65] 

"""
import random

numGrade = int(input("Enter the number of grades in the list: "))

grades = [random.randint(1,100) for _ in range(numGrade)]

passingGrade = int(input("Enter the passing grade: "))

passGrades = [grade for grade in grades if grade >= passingGrade]

print(f"Updated List: {passGrades}\nOriginal List: {grades}")

# for grade in grades:
#     grade = random.randint(0,100)

#     grades.append(grade)
# print(grades)

    # startCount = 0

    # while startCount < numGrade:

    #     startCount += 1
    #     print(grade)
    #     grades.append(grade)
# print(grades)


# passingGrade = int(input("Enter the passing grade: "))

# grades = list(random.randint(0,100))

# start = 0

# for grade in grades:
    
#     while start <= numGrade:
#         start += 1

#         grades.append(grade)
# print(grades)