# Write a python program that counts from from to 1000000
# while loop

"""
LIMIT = 100

counter = 0
while counter <= LIMIT:
    print("I love Syermen")
    counter = counter + 1
else:
    print("Loop ended")
"""

"""
counter = 0
name = "Faith Olaniran"
size = len(name)
while counter < size:
    print(name[counter].upper(), end="\n")
    counter = counter + 1
"""

"""LIMIT = 100

counter = 1
# Even number printed
while counter < LIMIT:
    if counter % 2 == 0:
        print("{} is even".format(counter), end="\n")
    elif counter % 2 == 1:
        print("{} is odd".format(counter), end="\n")
    counter = counter + 1"""

# for loop
#numbers = range(10)

"""for number in range(10):
    if number % 2 == 0:
        print("Lucky numbers {}".format(number))"""

for character in "Faith Olaniran":
    print(character.upper())

for number in range(20):
    print ("{:b}".format(number), end=", ")

for i in range(23):
    if i <=10:
        print(i)
        #break (When there is break the else statement will never execute)
        continue
    else:
        print("Loop ended")

    for i in range(12):
        for j in range(12):
            print("{} * {} = {}".format(i, j, (i * j)))