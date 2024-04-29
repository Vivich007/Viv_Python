age = 20
if age > 18:
    print("You are an adult")
elif age < 18 and age > 12:
    print("You are a teenager")
else:
    print("You are a minor")

# OR

age = 12
status = "adult" if age > 18 else "child"
print(status)

# Concatenation

greeting = "Hello"
name = "Alice"
message = greeting + " " + name
print(message)

# String Formatting

first_name = 'Viv'
last_name = 'Ogb'
fullname = "{} {} is a devops engineer." .format (first_name, last_name)
#fullname = f"{first_name} {last_name} is a devops engineer."
print(fullname)

# Read, Write, Append

# Error Handling (Exceptions)
result = 10/3
print(result)

try:
    result - 10/0
except ZeroDivisionError:
    result = "Error: Division by zero"
finally:
    
    result = "Something went wrong"

print(result)


def calculate(a, ):
    try:
        result - a/b
    except ZeroDivisionError:
        print("Error: Division by zero")
    finally:
        print("Something went wrong")

    print(result)


# List Comprehensions
# Dictionaries have key:value pairs using curly brackets, while
#Lists are index-spaced using square brackets
# Example: dog_deets = {'name':'Rex', 'age':4, 'colour':'brown'}  # dictionary
# https://www.w3schools.com/python/python_lists_comprehension.asp

numbers = [1, 2, 3, 4, 5, 6]
squared = [return x ** 2 for x in {numbers} if x%3 =0]

# Generators
# uses 'yield' for output


# Object-Oriented Programming (OOP)
# See screenshot in Macbook photos

# Decorators

# Context Managers
