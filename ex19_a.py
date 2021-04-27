# function with 2 arguments,  amount
def bacon_and_eggs(bacon_count = 50, eggs_count = 100):
    # print the f-string with the bacon_count
    print(f"You have {bacon_count} pieces of bacon!")
    # print the f-string with the eggs_count amount
    print(f"You have {eggs_count} amount of eggs!")
    # print a constructed string
    print("Man that's enough for a party")
    # print to get a blanket
    print("Get a blanket.\n")

# print that we can give the arguments directly
print("We can just give the function numbers directly:")
# call the function to run it, give in the arguments
bacon_and_eggs(40, 25)

# print that we can also use variables to use as arguments
print("OR, we can use variables from our script:")
# put 10 in amount_of_bacon
amount_of_bacon = 23
# put 50 in amount_of_eggs
amount_of_eggs = 74

# call the function to run it, give in the arguments
bacon_and_eggs(amount_of_bacon, amount_of_eggs)

# print that we can even use math inside the parantheses
print("We can even do math inside too:")
# call the function to run it, give in the arguments with doing some math
bacon_and_eggs(5 + 17, 1 + 3)

# print that we can do both variables and math
print("And we can combine the two. variables and math:")
# call the function to run it, give in the arguments as variables and do some math with them
bacon_and_eggs(amount_of_bacon + 115, amount_of_eggs + 550)

# ask the user for the amounts
bacon = int(input("Give me the available amount of bacon: "))
eggs = int(input("Give me the available amount of eggs: "))
# call the function to run it with the user input data
bacon_and_eggs(bacon, eggs)

# call the function with the standard amounts that is used by the arguments
bacon_and_eggs()

# call the function with different amounts
bacon_and_eggs(4, 28)
bacon_and_eggs(2, 37)
bacon_and_eggs(81, 79)
bacon_and_eggs(187, 245)