# set intitial values
people = 50
cars = 25
trucks = 35

# check if cars is greater then people
if cars > people:
    # if cars is greater, print the string
    print("We should take the cars.")
# check if people is greater then cars  
elif cars < people:
    # if people is greater, print this string
    print("We can't decide.")
# if cars and people are equal, print the string
else:
    print("We can't decide.")

# check if trucks is greater then cars
if trucks > cars:
    # if trucks is greater, print the string
    print("That's too many trucks.")
# check if cars is greater then trucks
elif trucks < cars:
    # if cars is greater, print the string
    print("Maybe we could take the trucks.")
# if cars and trucks are equal, print the string
else:
    print("we still can't decide.")

# check if people is greater then trucks
if people > trucks:
    print("Alright, let's just take the trucks.")
# In all other cases, print the string
else:
    print("Fine, let's stay home then.")