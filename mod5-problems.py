#1. Prompt the user for a positive integer n. Use a while loop to sum all the integers from 1 up to n. Print the final sum.

num = int(input("Please enter a positive interger: "))

if num > 0:
    count = 1
    sum = 0

    while count <= num:
        sum += count
        count += 1
else:
    print("Please provide valid input.")
print(sum)
    
#2. Define a string variable (e.g., my_string = "Olympic College"). Use a for loop to print each character on its own line. Convert each character to uppercase before printing.

string = "Andromeda Galaxy"

for char in string:
    print(char.upper())

#3. Use a for loop and the range() function to print all even numbers from 2 to 20.

for i in range(2,21):
    if i % 2 == 0:
        print(i)

#4. Use nested for loops to create a simple multiplication table for numbers 1 through 5. Format your output so that each row corresponds to multiplying by a specific number. Example output:

for i in range(1,6):
    for j in range(1,6):
        print(i * j, end=" ")
    print("\n")
    
#5. Write a program that continuously asks the user to input a number. If the user enters 0, immediately stop asking for more numbers. Otherwise, print the number they entered. Sample interaction:

i = int(input("please enter a number (0 to stop): "))
print("You entered ", i)

while i != 0:
    i = int(input("please enter a number (0 to stop): "))
    print("You entered ", i)
    
    if i == 0:
        break