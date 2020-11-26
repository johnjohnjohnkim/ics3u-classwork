Exercise 34

number = int(input("Enter an integer here: "))

if (number % 2) == 0: 
    print("\nThis is an even number obviously")
else: 
    print("\nThis is an odd number you dummy")


Exercise 35:

years = int(input("Please enter dog's age in human years: "))

if (0 <= years <= 2):
    child = 10.5 * years
    print(f"Your dog is {child} years old.")

if years > 2:
    (adult) = 21 + 4 * (years - 2)
    print(f"Your dog is {adult} years old.")

elif years < 0:
    print("Unavailable number, try again.")
    
    
Exercise 36:

letter = input("Please enter a letter of the alphabet: ")

if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
    print("Vowel")
elif letter == "y":
    print("Vowel when it feels like being a vowel")
else:
    print("Consonant")
    
Exercise 37:

shape = int(input("Number of sides of the shape: "))
print("")
if shape == 3: 
    print("Triangle")
if shape == 4: 
    print("Square")
if shape == 5: 
    print("Pentagon")
if shape == 6: 
    print("Hexagon")
if shape == 7: 
    print("Heptagon")
if shape == 8: 
    print("Octagon")
if shape == 9:
    print("Nonagon")
if shape == 10:
    print("Decagon")
    
Exercise 38: 

month = input("Enter your month: ")

if month == "January" or month == "March" or month == "May" or month == "July" or month == "August" or month == "October" or month == "December":
    print("31 days")
elif month == "April" or month == "June" or month == "September" or month == "November":
    print("30 days")
elif month == "February":
    print("28, 29 on leap years")
