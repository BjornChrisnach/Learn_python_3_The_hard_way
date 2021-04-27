# Ask the user to type in his age
print("How old are you?", end=' ')
# Store the input in the variable age
age = input()
# age = int(input())
print(">>>> age=", repr(age))
# ask the user his length
print("How tall are you?", end=' ')
# store the input in height
height = input()
# ask the user for his weight
print("How much do you weigh?", end=' ')
# store the input in weight
weight = input()

# Study drill
num = input("Enter your lucky number: ")
name = input("Enter your name :")

# print the formatted string, that holds age, height and weight
print(f"So, you're {age} old. {height} tall and {weight} heavy.")
# Study drill
print(f"Your lucky number is {num}, and your name is {name}")