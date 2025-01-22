# 1. Prompt the user for a word. Then, prompt the user for how many times they'd like that word repeated. Use the skills you learned in this module to print the word the correct number of times.
# Prompt the user for a word
word = input("Please enter a word: ")

# Prompt the user for the number of repetitions
repetitions = int(input("How many times would you like the word repeated? "))


 # Print the word the specified number of times
print(word * repetitions)


#2. Prompt the user for their name and their age. Calculate their age next year. Use string concatenation to print "Hello, <name>! You are <age1> years old. Next year, you will be <age2> years old."
#prompt for name and age
name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
# Calculate age next year
AgeNextYear = age + 1
#print
print(f"Hello {name}! You are {age} years old. Next year, you will be {AgeNextYear} years old.")
#3. Prompt the user for a sentence and a word to try to find in that sentence. Have the program print out whether the word was found in the sentence. (i.e. True or False)
# Prompt the user for a sentence
sentence = input("Please enter a sentence: ")

# Prompt the user for a word to find
word = input("Please enter a word to find in the sentence: ")

# Check if the word is in the sentence
word_found = word in sentence

# Print the result
print(f"Word found: {word_found}")

#4. Prompt the user for: a word, a first index, and a last index. Slice the word at the indexes provided by the user and print to the screen.
# Prompt the user for a word
word = input("Please enter a word: ")

# Prompt the user for the starting and ending indexes

start_index = int(input("Enter the starting index: "))
end_index = int(input("Enter the ending index: "))

 # Slice the word using the provided indexes
sliced_word = word[start_index:end_index]

    # Print the result
print(f"The sliced word is: {sliced_word}")

#5. Print 3 words with a | character (called a pipe) in between them. Use the appropriate keyword argument in print() to do so.
word1 = input("Please enter word 1: ")
word2 = input("Please enter word 2: ")
word3 = input("Please enter word 3: ")
print(word1, word2, word3, sep="|")