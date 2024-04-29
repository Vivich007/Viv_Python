# TASK 1
# Declare three variables with their values
print('TASK 1')

num1 = 10
num2 = 2.5
name = 'Vivich'

# Print the values of the variables
print(num1)
print(num2)
print(name)

# Print the types of the variables
print(type(num1))
print(type(num2))
print(type(name))



# TASK 2
print(' ')
print('Task 2')

# Prompt user to enter their age & store as a variable

age = int(input('Enter your age: '))    

# Print a message based on the age

if age < 18:
    print('You are a minor')
elif age >= 18 and age < 65:
    print('You are an adult')
else:
    print('You are a senior citizen')




# TASK 3
print(' ')
print('Task 3')

# Conditional Statements
# Write a function that takes a number checking parameter & checks if the number is -ve or +ve.

def check_number(num):
    if num > 0:
        print("Positive number.")
    elif num < 0:
        print("Negative number.")
    else:
        print("Zero.")

# Call this function with different integer values to test it.        
check_number(8)
check_number(-7)
check_number(0)


# TASK 4
print(' ')
print('Task 4')
#Write a loop that prints all even numbers from 0 to 20 (inclusive).
for num in range(1, 21):
    if num % 2 == 0:
        print(num)



# TASK 5
print(' ')
print('Task 5')

# Write a function that takes a single parameter (a float).

def calculate_circle_area(radius):
    pi = 3.14
    area = pi * radius ** 2
    return area

# Test the function with different radius
r1 = 2.0
r2 = 10.2
r3 = 3.5

area1 = calculate_circle_area(r1)
area2 = calculate_circle_area(r2)
area3 = calculate_circle_area(r3)

print(f"Area of circle with radius {r1} = {area1}")
print(f"Area of circle with radius {r2} = {area2}")
print(f"Area of circle with radius {r3} = {area3}")
