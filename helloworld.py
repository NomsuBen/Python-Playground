print("Hello world - I am loving ISWE")
#print("Benjamin Olaniran")
print("3")

#This is a single line comment
print("This is lovely")

"""
Ire is a fine boy
"""

#Variables - are use to store data
# = is an assignment symbol 
# Variables are case sensitive like customer, CUSTOMER, Customer and cUstomer are not the same because they are case sensitive

name = "Benjamin Olaniran"
age = 33
location = "Oyo"
country = "Nigeria"

learner = "Faith Olaniran"

customer = "Buyeke"
amount = 60
height = 20.1

#It shows the type of data that has been stored in a container 
print(type(customer))
print(type(amount))
print(type(height))

"""
Data Types:
Text type: string(str) e.g "cole" "1000"
Numeric type: int, float, complex e.g 55, 45.77 56g
Sequence type: list, tuple, range
Mapping type: Dictionary dict
Set: set frozenset
Boolean: bool - True or False
None type: NoneType
Data types is important because whenever you create a variable you must have a data type stored in it
"""

#String Type
name = "Benjamin Olaniran"
size = len(name)
lowercase = name.lower #Lower case function
rep = name.replace("B", "b") #Replacing B with b
#print(rep + " has " + str(size) + " Characters ")
print("{} has {}" .format(rep, size))

#slice = name[0] #Slicing allowed you to access each charater in a string
#slice = name[size - 2] # this will give the second letter by the rear(from the end)
#slice = name[:7]#This will print everything from 0 - 6th index
#slice = name[2:]#This will omit the the first 2 letter and print the remaining
slice = name[5:8]
print(slice)




name = "Benjamin"
age = 33
height = 11.8
imaginary = 3j

CUSTOMER = "Joel"
product = "Iphone 11"
price = 1000
print("Customer name: "+ CUSTOMER)
print("product name: " + product)
#print("Price: " + str(price)) #Casting is converting an integer to string


"""
TypeCasting
int() - Any value to an integer 
float() - Any value to a decimal of floating point number
str() Any value to string
"""