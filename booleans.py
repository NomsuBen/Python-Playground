#True
#False

#print(type(True))
#print(type("True"))

"""
Booleans
print(4 != 5)

Decicion
"""
VOTING_LIMIT = 18
age = int (input("How old are you "))

if age >= VOTING_LIMIT:
    print ("You can vote")
else:
    print("Please check again when you are 18+ ")

#Logical operator
# 

VOTING_LIMIT = 18
HEIGHT_LIMIT = 6
age = int (input("How old are you "))
height = int(input("What is your height in feets "))

if age > VOTING_LIMIT and height > HEIGHT_LIMIT:
    print ("You can vote")
elif age == VOTING_LIMIT and height == HEIGHT_LIMIT:
    print("You are the perfect match to vote")
else:
    print("Please check again when you are 18+ ")

