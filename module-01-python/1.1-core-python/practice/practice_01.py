# Write a program that stores your information
name: str = " Adesco"
age: int= 32
height: float = 1.75
learning_python: bool = True


print("My name is", name)
print("My age is", age)
print("My height is", height)
print("I am learning Python:", learning_python)

# Practice 2
# Predict the output before running this:
'''
x = "10"
y = 5

print(x + str(y))
print(int(x) + y)
'''

# Practice
# Exercise 1: Grade calculator
# Write a program that prints:

# "A" for scores from 90 to 100.
# "B" for scores from 80 to 89.
# "C" for scores from 70 to 79.
# "D" for scores from 60 to 69.
# "F" for scores below 60.

"""solution for grade calculator"""
student_score = int(input("Enter student score: "))

if student_score >= 90:
    grade = "A"
elif student_score >= 80:
    grade = "B"
elif student_score >= 70:
    grade = "C"
elif student_score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Grade: {grade}")


# Exercise 2: Number loop
# Print the numbers from 1 to 20, but:

# Print "even" for even numbers.
# Print "odd" for odd numbers.
# Hint:

# python


# number % 2 == 0
# Exercise 3: Comprehension
# Create a list containing the cubes of numbers from 1 through 10:

# python


# cubes = [number ** 3 for number in range(1, 11)]
# Then create a list containing only the cubes that are greater than 100.

# Exercise 4: Password attempts
# Create a program that gives the user three attempts to enter the correct password.

# python


# correct_password = "python123"
# Use a loop, if, and break.

# Send your solutions when finished, and they can be checked before moving to functions.
