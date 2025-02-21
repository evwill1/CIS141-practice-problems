#1. Write a function called count_vowels(input) that takes a string
#and returns the number of vowels (a, e, i, o, u) in it.

def count_vowels(input):
    count = 0
    vowels = "aeiouAEIOU"
    for char in input:
        if char in vowels:
            count += 1
    print(count)
        
        
            
user_input = input("Please enter a string: ")
count_vowels(user_input)




# #2. Write a function called is_palindrome(s) that checks whether a string is a
# palindrome
# (reads the same forward and backward, ignoring case). The function should
# returns
# either True or False.

def is_palindrome(string):
    
    reverse = string[::-1]
    
    if string == reverse:
        print(True)
    else:
        print(False)
        
user_input = input("please enter a string: ")
is_palindrome(user_input)

# #3. In the game Pokemon, certain types of Pokemon do extra damage to other types.
# For example, water is very effective to fight fire.
# Write a function called type_advantage(attacker, defender) that takes two
# Pokémon types as
# strings and returns "Super Effective", "Not Very Effective", or "Neutral" based
# on
# simple type effectiveness rules. Your solution only needs to work for these
# three sets of input:
# print(type_advantage("Water", "Fire")) # "Super Effective"
# print(type_advantage("Fire", "Water")) # "Not Very Effective"
# print(type_advantage("Electric", "Grass")) # "Neutral"

def type_advantage(attacker, defender):
    if attacker == "Water" and defender == "Fire":
        return "Super Effective"
    elif attacker == "Fire" and defender == "Water":
        return "Not Very Effective"
    elif attacker == "Electric" and defender == "Grass":
        return "Neutral"
    
print(type_advantage("Water", "Fire"))
print(type_advantage("Fire", "Water"))
print(type_advantage("Electric", "Grass"))

# #4. Write a function called ferry_fare(age, vehicle) that calculates the Washington
# State Ferry fare
# based on age and whether the person has a vehicle. Assume the following rates:
# * Adults (19-64): $10 without a vehicle, $20 with a vehicle.
# * Seniors (65+): $5 without a vehicle, $15 with a vehicle.
# * Children (0-18): Free.

def ferry_fare(age, vehicle):
    price = 0
    
    if int(age) < 19:
        price += 0
        vehicle == "No"
    elif int(age) < 65:
        price += 10
    elif int(age) < 64:
        price += 5
 
    if vehicle == "Yes":
        price += 10
    elif vehicle == "No":
        price += 0

    print("Your fare is $", price)
    
age = input("Please enter age: ")
if int(age) < 19:
    vehicle = "No"
    ferry_fare(age, vehicle)
elif int(age) > 18:
    vehicle =input("Do you have a vehicle? (Yes/No): ")
    ferry_fare(age, vehicle)

# #5. Write a function called level_up(experience) that takes a player's experience
# points
# and returns their new level based on these rules:
# * 0-99 XP → Level 1
# * 100-199 XP → Level 2
# * 200+ XP → Level 3

def level_up(experience):
   
    if experience < 100:
        return "Level 1"
    elif experience < 200:
        return "Level 2"
    else:
        return "level 3"
   
xp = int(input("Please enter your XP: "))

print(level_up(xp))