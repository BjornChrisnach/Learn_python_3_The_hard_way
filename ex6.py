# Stores a value of 10 in the types_of_people variable
types_of_people = 10
# Stores the formated string inside of x
x = f"There are {types_of_people} types of people."

# Stores the value "binary" inside the variable binary
binary = "binary"
# Stores the value "don't" inside the variable do_not
do_not = "don't"
# Stores the formated string inside the variable y
y = f"Those who know {binary} and those who {do_not}"

# prints the variable x
print(x)
# prints the variable y
print(y)

# prints the formated string with use of the variable x
print(f"I said: {x}")
# prints the formated string with use of variable y
print(f"I also said: '{y}'")

# stores the value False inside of hilarious
hilarious = False
# stores the formated string inside the variable joke_evaluation, without specifying the formating parameter
joke_evaluation = "Isn't that a joke so funny?! {}"

# prints the variable joke_evaluation and gives the formated parameter hilarious
print(joke_evaluation.format(hilarious))

# stores a string value in w, beeing the left side of a later string concationation
w = "This is the left side of..."
# stores a string value in e, beeing the right side of a later string concationation
e = "a string with a right side"

# prints the concationated values of the variables w and e
print(w +e)

# Study drills
# 4) Convationating a string puts the 2 strings together forming a longer string