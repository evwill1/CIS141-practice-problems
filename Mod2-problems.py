# import math functions
import math

# 1. Create a program that prints the following output to the screen: 
# "Water. Earth. Fire. Air. Long ago, the four nations lived together in harmony. Then, everything changed when the Fire Nation attacked."
print("Water. Earth. Fire. Air. Long ago, the four nations lived together in harmony. Then, everything changed when the Fire Nation attacked.")

# 2. Create a program that prompts for 2 numbers and then outputs the addition, subtraction, multiplication, and division of the first number by the second number.

# Get first number
print("This is a calculator that will add, subtract, mulitply and divide two user entered numbers.")
int1 = int(input("Please enter your first number: "))
print("Your first number is:", int1)
# Get second number
int2 = int(input("Please enter your second number: "))


# Calculations
int3 = int1 + int2
int4 = int1 - int2
int5 = int1 * int2
int6 = int1 / int2

# Display results
print (f"{int1} + {int2} = {int3}")
print (f"{int1} - {int2} = {int4}")

print (f"{int1} x {int2} = {int5}")
print (f"{int1} ÷ {int2} = {int6:.2f}")

# 3. Create a program that prompts for the side lengths of a triangle and computes the area using Heron's formula. (https://en.wikipedia.org/wiki/Heron%27s_formula)

print("This is a calculator to compute the area of a triangle using Heron's Formula")

# Gather user inputs

sideA = float(input("Please enter side 'A' of the triangle: "))
sideB = float(input("Please enter side 'B' of the triangle: "))
sideC = float(input("Please enter side 'C' of the triangle: "))

# Ensure inputs are valid to agree with triangle inequality theorem


print(f"You entered {sideA} for side 'A', {sideB} for side 'B', and {sideC} for side 'C'.")

 # Calculate semiperimeter

s = 0.5 * (sideA + sideB + sideC)

# Calculate area

area = math.sqrt(s * (s - sideA) * (s - sideB) * (s - sideC))

print(f"The area of your triangle is {area:.2f}")

# 4. Create a program that computes different statistics given five numbers including the total, average, minimum, maximum, range, and standard deviation (https://en.wikipedia.org/wiki/Standard_deviation).

print("This program computes different statistics when given five numbers including the total, average, minimum, maximum, range, and standard deviation.")

# Gather user inputs

value1 = float(input("Enter first value: "))
value2 = float(input("Enter second value: "))
value3 = float(input("Enter third value: "))
value4 = float(input("Enter fourth value: "))
value5 = float(input("Enter fifth value: "))

# Calculate total

total = value1 + value2 + value3 + value4 + value5
print(f"The total is {total}.")

# Calculate average

avg = total / 5
print(f"The average is {avg}.")

# Calculate minimum

minimum = min(value1, value2, value3, value4, value5)
print(f"The minimum value is {minimum}.")

# Calculate maximum

maximum = max(value1, value2, value3, value4, value5)
print(f"The maximum value is {maximum}.")

# Calculate deviations

value6 = (value1 - avg) ** 2
value7 = (value2 - avg) ** 2
value8 = (value3 - avg) ** 2
value9 = (value4 - avg) ** 2
value10 = (value5 - avg) ** 2

# Calculate variance

var = (value6 + value7 + value8 + value9 + value10) / 5

# Calculate standard deviation

std_dev = math.sqrt(var)
print(f"The standard deviation of the values is {std_dev:.2f}.")