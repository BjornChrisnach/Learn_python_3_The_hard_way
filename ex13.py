from sys import argv
# read the WYSS section for how to run this
script, first, second, third = argv

print(">>>> argv=", repr(argv))

name = input("Type in your name: ")
age = input("What is your age? ")

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

print(f"Your name is {name} and you're {age} years old.")