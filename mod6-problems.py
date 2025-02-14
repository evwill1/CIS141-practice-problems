#1. Given a list of numbers, write code to iterate through the list and calculate the sum of all even numbers. Print the resulting sum.
numbers = [1, 4, 7, 3, 5, 9, 0, 2, 1, 6]

sum = 0

for i in numbers:
    if i % 2 == 0:
        sum += i
        
print("The sum of all even numbers:", sum)

#2. With a list of strings provided, write code that counts how many times the word "Olympic" appears in the list, and then print the count.
numbers = ["Olympic", "College", "Olympic", "College", "Olympic", "College", "College", "College", "Olympic", "College"]

sum = 0

for word in numbers:
    if word == "Olympic":
        sum += 1
        
print("Olympic is in the string", sum, "times.")

#3. Given a list of strings, write code to create a new list that includes only the strings longer than three characters. Print the resulting filtered list.
words = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
new_words = []

for word in words:
    if len(word) > 3:
        new_words.append(word)
        
print(new_words)
        
#4. For a list of integers, write code that counts how many numbers are positive and how many are negative, then print both counts.
numbers = [-5, 2, -9, -1, -8, -4, -3, -2, -7, -3]

neg_int = 0
pos_int = 0

for i in numbers:
    if i > 0:
        pos_int += 1
    if i < 0:
        neg_int += 1
        
print("the total number of positive intergers is: ", pos_int)
print("the total number of negative intergers is: ", neg_int)

#5. For a list of integers, use a loop to build a new list where each element is the square of the corresponding element in the original list. Print the new list.
import math
numbers = [4, 64, 49, 25, 100, 144, 36, 81, 121]
squared_numbers = []

for i in numbers:
    root = int(math.sqrt(i))
    squared_numbers.append(root)

print(squared_numbers)