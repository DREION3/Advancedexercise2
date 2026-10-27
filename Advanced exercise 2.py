# Advanced Exercise 2.py
# Advanced Python challenge exercise 2
# Question: Write a Python program that takes a list of numbers and returns a new list containing only the even numbers from the original list.
a = 5
b = 10
c = 7
# add 3 to a using the += operator
a += 3
a = 8
#multiply b by 2 using the *= operator
b *= 2
b = 20
#modulus c by 3 using the %= operator
c %= 4
c = 3
#calculate the square root of (a^2 + b^2 + c^2) using the math.sqrt() function
import math
result = math.sqrt(a**2 + b**2 + c**2)
(a**2 + b**2 + c**2) = 42
result = math.sqrt(42)
# print 
print (round(result, 2))

# Question 2: Complex conditional Evaluation
x = int(input("Enter the first integer (x): "))
y = int(input("Enter the second integer (y): "))
z = int(input("Enter the third integer (z): "))
#print
print(f"x is even: {x % 2 == 0}")
print(f"y is positive: {y > 0}")
print(f"z is between 10 and 50: {10 < z < 50}")

# Combine the conditions using logical operators
combined_result = (x % 2 == 0) and (y > 0) and (10 < z < 50)
print(f"All conditions met: {combined_result}")

is_even = x % 2 == 0
is_positive = y > 0
is_in_range = 10 < z < 50
final_condition = is_even and is_positive and is_in_range
print(f"Final condition met: {final_condition}")

#Question 3: Grading with Adjustments
# -------------------------------------------

# Task:
# Ask the user for their base score, then apply:
# - bonus points (+5)
# - late penalty (-10)
# Final score must not exceed 100 or drop below 0.
# Then assign a grade.

# Tip: Use min() and max() to constrain the score.


# TODO: Input score from user
base_score = float(input("Enter your base score: "))
# TODO: Apply adjustments
final_score = base_score + 5 - 10
# TODO: Clamp score between 0 and 100
final_score = max(0, min(100, final_score))
# TODO: Use if-elif-else to determine grade and print it

if final_score >= 80:
    grade = "A"
elif final_score >= 60:
    grade = "B"
else:
    grade = "C"

#Print final score and grade
print(f"Your final score is {final_score} and your grade is {grade}.")      


#Question 4: Advanced Calculator
#task
#ask the users to input two numbers and an operator (+, -, *, /)
#Handle division/modulus by zero with try-except
#perform the operation and print the result
# todd :i
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter the operator (+, -, *, /): ")

try:
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Division by zero is not allowed.")
            result = None
    else
        print("Error: Invalid operator.")
        result = None

    if result is not None:
        print(f"The result of {num1} {operator} {num2} is: {result}")

except ValueError:
    #print

    print("Error: Please enter valid numbers.")