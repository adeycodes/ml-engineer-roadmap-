# LEARNING PYTHON FOR MACHINE LEARNING 
# print("Hello, World!")

# 1.1.1 — Variables, Types & Type Annotations
# A variable is a name holding a value. Python's core types: str (text), int (whole numbers), float (decimals), bool (True/False). Type annotations tell readers what type a variable is meant to hold
'''
name: str = "Adesco"
age: int = 32
height: float = 1.75
is_teacher: bool = True
# i just learnt a new way of writing a python code whereby the variable
# is declared wih a name inserting a column and declaring a datatype, and the values
print(name, age, height, is_teacher)

# the above code is an annotation of the  variables, and the below code is a normal way of declaring variables in python

'''
# a = None
# print(a)

# converting between data tyoes
# school = "100"
# school_int = int(school)

# print(school_int, type(school_int))

#  let identify all the data types in python
# class_name = "Python for Machine Learning" # str
# class_size = 30 # int
# class_duration = 1.5 # float
# is_class_active = True # bool
# None_value = None # NoneType

#the above are the main data types in python, and they are used to store different types of data in a program. The str data type is used to store text, the int data type is used to store whole numbers, the float data type is used to store decimal numbers, the bool data type is used to store True/False values, and the NoneType data type is used to represent the absence of a value.



# 1.1.2 — Control Flow (if/else, loops, comprehensions)
# control flow determines which codes runs how many times and in what order
# A. the most used key words is if/elif and else. It is used with logical operators and 
# comparison operators

# score = 85

# if score>= 90:
#     print("A")
# elif score >= 80:
#     print("B")
# else:
#     print("C")


# for loops for iterating through items in an array of data
# fruits = [ "Orange", "Pineapple"]

# for fruit in fruits:
#     print (f"list of fruits: {fruits}")

    
# for number in range(1,9):  # we use the range(start, stop) function for iterating through numbers 
#     if number >= 5:
#       print(f"value of number: {number}")
# count = 1

# while count <= 5:
#     print(count)
#     count -= 1 this code causes an infinite loop



# for number in range(1, 10):
#     if number == 5:   # this code will break the loop when the number is equal to 5: 1,2 3, 4
#         break
#     print(number)

# for number in range(1, 10):
#     if number == 5:   # this code will skip the number 5 and continue with the loop: 1,2,3,4,6,7,8,9
#         continue
#     print(number)


# comprehensions are a concise way to create lists, sets, or dictionaries in Python. They allow you to generate a new collection by applying an expression to each item in an existing iterable.
# list comprehension

squares =  []

for number in range(1, 6):
   squares.append(number ** 2)


print(squares)

# OR
squaress = [number * number  for number in range(1,6)]

print(squaress)




