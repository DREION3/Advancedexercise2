#advanced
#Advanced Python Challenge: Exercise 02 Operators and Condition
import math
# Question 1: Multi-Step Arithmetic Operations

#  base values
a = 5
b = 10
c = 7

#add 3 to a using +=
a+=3

#multiply b by 2
b*=2

#modullus of c by 3
c%=4

# Calculating the square root of (a^2 + b^2 + c^2)
#Input math

                  
                                          
# The square root 
result = math.sqrt(a**2 + b**2 + c**2)          

# print                             
print(round(result,2))              



# Question 2: Complex Conditional Evaluation
# Variable
# input integers
x = int(input("Enter the first interger (x):"))

y = int(input("Enter the second interger (y):"))

z = int(input("Enter the third interger (z):"))

is_even= x % 2 == 0
is_positive = y> 0
is_between_10_and_50 = 10 < z < 50



#final condition
final_condition = is_even and is_positive and is_between_10_and_50

#print
print(final_condition)

# Question 3: Grading with Adjustments

#Input score from user
base_score = int(input("Enter your base score"))
#Applying adjustments
#bonus points
base_score = int(input("Enter your base score")) +5

#late penality
base_score = int(input("Enter your base score")) -10

# Clamp score between 0 and 100
final_score = max(0, min(100, final_score )) # type: ignore

#  Use if-elif-else to determine grade and print it

if final_score >= 80:
    grade = "A"
elif final_score >= 60:
    grade = "B"
else:
    grade = "C"

#Print 
print(final_score,grade)


# Question 4: Advanced Calculator
num1 =int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
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
    else:
        print("Error: Invalid operator.")
        result = None

    if result is not None:
        print(f"The result of {num1} {operator} {num2} is: {result}")
except ArithmeticError as error:
    print("Error: {error}")
r valid numbers.")
