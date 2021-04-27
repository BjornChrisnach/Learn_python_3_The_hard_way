# function with 2 arguments, cheese and crackers amount
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # print the f-string with the cheese_count
    print(f"You have {cheese_count} cheeses!")
    # print the f-string with the boxes_of_crackers amount
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    # print a constructed string
    print("Man that's enough for a party")
    # print to get a blanket
    print("Get a blanket.\n")

# print that we can give the arguments directly
print("We can just give the function numbers directly:")
# call the function to run it, give in the arguments
cheese_and_crackers(20, 30)

# print that we can also use variables to use as arguments
print("OR, we can use variables from our script:")
# put 10 in amount_of_cheese
amount_of_cheese = 10
# put 50 in amount_of_crackers
amount_of_crackers = 50

# call the function to run it, give in the arguments
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# print that we can even use math inside the parantheses
print("We can even do math inside too:")
# call the function to run it, give in the arguments with doing some math
cheese_and_crackers(10 + 20, 5 + 6)

# print that we can do both variables and math
print("And we can combine the two. variables and math:")
# call the function to run it, give in the arguments as variables and do some math with them
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)