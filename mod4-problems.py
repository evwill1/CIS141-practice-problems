#1. Construct a truth table for the expression: (A AND B) OR (NOT B) where A and B each can be True or False. Your truth table should be commented out (as it's not valid Python code!)

#AND operator &&
#A      B       A AND B
#-------------------------
#true   True    True
#true   False   False
#False  True    False
#False  False   False

#2. The headlights of a car should only automatically turn on when the daylight outside is below a certain threshold. If a sensor threshold is below the number 8, print "Headlights On"; otherwise, print "Headlights Off".

sensor_threshold = float(input("On a scale of 1-20, please enter the intensity of sunlight: "))
print(sensor_threshold)

if sensor_threshold <1 or sensor_threshold >20:
    print("Please enter a proper value.")
elif sensor_threshold <8:
    print("Headlights On")
else:
    print("Headlights Off")
    
#3. Prompt the user for their bank balance. Evaluate whether the balance is less than $100. Print True if the user’s balance is below $100; print False, otherwise.

balance = float(input("Please enter bank balance: $"))

print(f"Balance: ${balance:.2f}")

print("Value less than $100?")
if balance < 100:
    print(True)
else:
    print(False)

#4. A theater wants to enforce age restrictions for movie tickets. Ask the user for their age, and tell them whether they can see G (appropriate for under 13), PG-13 (appropriate for 13 to 17), or R (appropriate for over 18) rated movies.

age = int(input("Please enter your age: "))
print(f"You entered your age: {age}")

if age < 13:
    print("You are allowed admittance to G rated movies.")
elif age <= 0:
    print("Please enter a valid age.")
elif age < 18:
    print("You are allowed admittance to G and PG-13 rated movies.")
else:
    print("You are allowed admittance to G, PG-13, and R rated movies.")


#5. A store charges $5 for shipping on any order under $50. If the order amount is $50 or more, shipping is free. Ask the user for the order total and print the total cost, including shipping.

order_amount = float(input("Please enter the order amount: $"))
print(f"You entered order amount: ${order_amount:.2f}")
shipping = 5
with_shipping = order_amount + shipping
without_shipping = order_amount


if order_amount < 50:
    print(f"With a $5 shipping charge your total is: ${with_shipping:.2f}")
else:
    print(f"You saved $5 in shipping! Your total is: ${without_shipping:.2f}")