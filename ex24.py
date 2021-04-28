# print some text to the output window
print("Let's practice everything.")
print('You\'d need to know \'bout escapes with \\ that do:')
print('\n newlines and \t tabs.')

# assign this text into the variable poem
poem = """
\tThe lovely world
with logic so firmly planted
canot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""
# print the dash line and print what's in poem
print("----------")
print(poem)
print("----------")

# do some math and store it in the five variable
five = 10 - 2 + 3 - 6
# print the contents of the five variable
print(f"This should be five: {five}")

# define a function with argument started
def secret_formula(started):
    # do some math on started and store in jelly_beans
    jelly_beans = started * 500
    # do some math on jelly_beans and store in jars
    jars = jelly_beans / 1000
    # do some math on jars and store in crates
    crates = jars / 100
    # return jellbbeans, jars and crates and exit the function
    return jelly_beans, jars, crates

# set a number to start_point
start_point = 10000
# unpack the return statement from the function call to 
# secret_formula with the given start point 
beans, jars, crates = secret_formula(start_point)

# remember that this is another way to format a string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

# set a value into start_point
start_point = start_point / 10

# print about the different ways to do stuff
print ("We can also do that this way:")
# store the return value (a list) from the call to secret_formula in 
# the variable formula
formula = secret_formula(start_point)
# this is an easy way to apply a list to a format string
# us the asterisk together with the list formula, like *formula
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))