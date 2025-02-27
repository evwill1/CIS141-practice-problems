# #1. Create a file called gardening_tips.txt and add at least 3 gardening tips to
# it.
# Write a Python script that reads a file gardening_tips.txt and prints
# out each tip one by one.

file = open("gardening_tips.txt", "r")
content = file.read()
print(content)
file.close()

#2. Write a Python program that allows users to log their hiking trips. The program
# should:
# - Use a while loop to repeatedly ask for a hike name and distance in miles
# - Save each entry to hiking_log.txt (each hike on a new line)
# - When the user presses 0, exit the loop & print the contents of hiking_log.txt

while True:
    hike_name = input("Enter hike name (0 to exit): ")
    if hike_name == "0":
        break
    distance = input("Enter distance in miles for this hike: ")
    file = open("hiking_log.txt", "a")
    file.write(hike_name + " - " + str(distance) + "\n")
    
print("Hiking Log:")
file = open("hiking_log.txt", "r")
print(file.read())
file.close()

# #3. Create a text file called song_lyrics.txt and copy the lyrics of a song into
# it. Write a Python program that:
# - Reads the file
# - Requests 5 inputs from the user: 5 words the user would like to count the
# frequency of
# - Counts how many times each word appears
# - Creates a dictionary of the words and their counts
# - Print the dictionary to the console

# Open file
file = open("song_lyrics.txt", "r")
print(file.read())

# Get user input for words
word1 = input("Please enter word 1: ")
word2 = input("Please enter word 2: ")
word3 = input("Please enter word 3: ")
word4 = input("Please enter word 4: ")
word5 = input("Please enter word 5: ")

# set word counters to 0
word1_count = 0
word2_count = 0
word3_count = 0
word4_count = 0
word5_count = 0

# Open file
with open("song_lyrics.txt", "r") as file:
    
    # Search lines in file
    for line in file:
        
        # Split lines into words
        for word in line.split():
            
            # Check for words in song lyrics
            if word == word1:
                word1_count += 1
            elif word == word2:
                word2_count += 1
            elif word == word3:
                word3_count += 1
            elif word == word4:
                word4_count += 1
            elif word == word5:
                word5_count += 1
                
# Create dictionary for words: count. 
word_count = {
    }

word_count[word1] = word1_count
word_count[word2] = word2_count
word_count[word3] = word3_count
word_count[word4] = word4_count
word_count[word5] = word5_count

# Print dictionary
for word, count in word_count.items():
    print(f"Word: {word}, Count: {count}")
file.close()


# #4. Create a poll.txt file that contains a list of "yea" or "nay" votes separated
# by commas.
# Write a program that reads the poll.txt file
# Count how many votes "yea" or "nay" received and print the results.

# Start vote counts at 0
yea = 0
nay = 0

# Open poll.txt
with open("poll.txt", "r") as file:
    
    # Read content
    content = file.read()
    # check for votes in poll.txt
    for word in content.split(","):
        
        # remove extra characters
        vote = word.strip() 
        
        #check for votes and add to counter
        if vote == "yea":
            yea += 1
        elif vote == "nay":
            nay += 1
            
# Print total votes
print("Total yea: ", yea)      
print("Total nay: ", nay)

# close file   
file.close()