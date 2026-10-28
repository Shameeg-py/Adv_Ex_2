# -------------------------------------------
# Advanced Python Challenge: Exercise 02 Operators and Conditionals
# -------------------------------------------


# -------------------------------------------
# Question 1: Multi-Step Arithmetic Operations
# -------------------------------------------



import math

# Start with some base values
a = 5
b = 10
c = 7

# TODO: Add 3 to a using +=
a+=3
print(a)
# TODO: Multiply b by 2 using *=
b*=2
print(b)
# TODO: Modulo c by 4 using %=
c%=4
print(c)
# TODO: Calculate the square root of (a^2 + b^2 + c^2)
root= math.sqrt ((a ** 2) +  (b ** 2) + (c ** 2))
# TODO: Print the final result rounded to 2 decimal places
rounded_root= round(root, 2)
print(rounded_root)

# -------------------------------------------
# Question 2: Complex Conditional Evaluation
# -------------------------------------------



# TODO: Input x, y, z
x= int(input("Please input a value for x: "))
y= int(input("Please input a value for y: "))
z= int(input("Please input a value for z: "))
# TODO: Create conditions:
#   is_even = True if x is even
if x % 2 ==0:
  is_even= True
else:
  is_even=False
print(is_even)
#   is_positive = True if y > 0
if y > 0:
  is_positive=True
else:
  is_positive= False
print(is_positive)
#   is_in_range = True if z between 10 and 50
if z >=10 and z <=50:
  is_in_range= True
else:
  is_in_range=False
print(is_in_range)
# TODO: Create final_condition = is_even and is_positive and is_in_range

final_condition= is_even and is_positive and is_in_range

# TODO: Print final_condition
print(final_condition)

# -------------------------------------------
# Question 3: Grading with Adjustments
# -------------------------------------------



# TODO: Input score from user
base_score= int(input("Please input your base score: "))
# TODO: Apply adjustments
new_score = base_score +5 -10
# TODO: Clamp score between 0 and 100
def clamp(new_score, minimum, maximum):
    if new_score < minimum:
        return "Invalid"
    elif new_score > maximum:
        return "Invalid"
    else:
        return new_score
print(clamp(new_score, 0 ,100))
# TODO: Use if-elif-else to determine grade and print it
if new_score >=101 or new_score <= 0:
    Grade = "Invalid"
elif new_score >= 90  and new_score <= 100:  
    Grade = "A"
elif new_score >= 80:
    Grade = "B"
elif new_score >= 70:
    Grade = "C"
elif new_score >= 60:
    Grade = "D"
elif new_score >= 50:
    Grade = "E"
else:
    Grade = "F"

print("Grade:", Grade)

# -------------------------------------------
# Question 4: Advanced Calculator
# -------------------------------------------



# TODO: Input num1, num2
num1= int(input("Please input a value for num1: "))
num2= int(input("Please input a value for num2: "))
# TODO: Input operation
operation= input("Please input a operation(+, -, *, /, %, **): ")
# TODO: Match operation using if-elif
if num2 == 0 and operation == "/" or operation== "%":
  result = "invalid"
elif operation == "+":
  result = (num1 + num2)
elif operation == "-":
  result = (num1 - num2)
elif operation == "*":
  result = (num1 * num2) 
elif operation == "%":
  result = (num1 % num2)
elif operation == "**":
  result =(num1 ** num2)
elif operation == "/":
  result = (num1 / num2) 
else:
  result = "Invalid Input"

# TODO: Handle division/modulus by zero with try-except
try:
    if operation == "+":
        result = (num1 + num2)
    elif operation == "-":
        result = (num1 - num2)
    elif operation == "*":
        result = (num1 * num2 )
    elif operation == "/":
        result = (num1 / num2)
    elif operation == "%":
        result = (num1 % num2)
    elif operation == "**":
        result = (num1 ** num2)
    else:
        result = "Invalid Operation"

except ZeroDivisionError:
    result = "Error: Division or modulus by zero is not allowed."
# TODO: Print result
print(result)
