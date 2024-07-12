# String data type
import math
print(" ")

# literal assignment
first = "Krystian"
last = "Stopka"
# print(type(first))
# print(type(first) == str)
# print(isinstance(first, str))


# constructor function
pizza = str("Pepperoni")
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))


# Concatenation
fullname = first + " " + last
# print(fullname)
fullname += "!"
# print(fullname)

# Cating a number to a string
decade = str(1980)
# print(type(decade))
# print(decade)

statement = 'I like rock music from the ' + decade + 's.'
# print(statement)

# Multiple lines
multiline = '''
Hey how are you?

I Was just checking in.

              All good?

'''
# print(multiline)

# Escaping special characters
sentence = 'I\'m back at work!\tHey!\n\nWhere\'s this at\\located?'
# print(sentence)


# String methods
# print(first)
# print(first.lower())
# print(first.upper())
# print(first)

# print(multiline.title())
# print(multiline.replace("good", 'ok'))

# print(len(multiline))
# multiline += "                       "
# print(len(multiline))
# multiline = "                       " + multiline
# print(len(multiline))

# print(len(multiline.strip()))
# print(len(multiline.lstrip()))
# print(len(multiline.rstrip()))


# Build menu
title = "menu".upper()
# print(title.center(20, '='))
# print("Coffe".ljust(16, ".") + "1$".rjust(4))
# print("Muffin".ljust(16, ".") + "4$".rjust(4))
# print("Cheesecake".ljust(16, ".") + "8$".rjust(4))

# print("")

# String index values
# print(first[0])
# print(first[-1])
# print(first[1:-1])
# print(first[1:])

# Some methods return boolean data

# print(first.startswith("K"))
# print(first.endswith("n"))
# print(first.endswith("Z"))

# boolean data type
myValue = True
x = bool(False)
# print(type(x))
# print(isinstance(myValue, bool))

# Numeric data types

# integer type

price = 100
bestPrice = int(80)
# print(type(price))
# print(isinstance(bestPrice, int))

# float Type
gpa = 3.28
y = float(1.14)
# print(type(gpa))

# complex type
comp_value = 5+3j
# print(type(comp_value))
# print(comp_value.real)
# print(comp_value.imag)

# Build-in functions for numbers
# print(abs(gpa))
# print(abs(gpa * -1))
# print(round(gpa))
# print(round(gpa, 1))
# print(round(gpa, 5))

print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))

# Casting a string a number

zipcode = "10001"
zip_value = int(zipcode)
print(type(zipcode))

# error if you attempt to cast incorrect data

# zip_value = int("New York")
