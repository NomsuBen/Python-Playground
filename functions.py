# def keyworld means to define function
# Creating/defining a function
# Name of the function
# parenthesis ()
# colon :
def helloWorld():
    print("Hello ALX iSWE")


# Call/invoke the function
helloWorld()


def howdy(user):
    print("Howdy {}".format(user))


howdy(user="Benji")


def area_of_room(length, width):
    return length * width


area = area_of_room(12.56, 234.21)
print("Area is {}".format(area))
