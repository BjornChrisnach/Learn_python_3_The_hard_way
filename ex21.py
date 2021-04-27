# a function to add 2 numbers
def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

# a function to subtract 2 numbers
def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

# a function to multiplying 2 numbers
def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

# a function to divide 2 numbers
def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b

# print a sentence about using the math
print("Let's do some math with just functions!")

# put the results from the function calls in variables
age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

# put the results from the function calls into variables
add_num = add(21, 61)
sub_num = subtract(154, 89)
mul_num = multiply(13, 11)
div_num = divide(111, 4)

# print the f-string with the age, height, weight and iq
print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

# A puzzle for the extra credit, type it in anyway.
print("Here is a puzzle.")

# broken down the long formula from below, put the results from the 
# function calls in variables
multiply_arg2 = divide(iq, 2)
subtract_arg2 = multiply(weight, multiply_arg2)
add_arg2 = subtract(height, subtract_arg2)
what = add(age, add_arg2)

# broken down the long formula from below, put the results from the 
# function calls in variables
multiply_arg2 = divide(div_num, 2)
subtract_arg2 = multiply(mul_num, multiply_arg2)
add_arg2 = subtract(sub_num, subtract_arg2)
result_num = add(add_num, add_arg2)

# a long formula, that sets the result as the second argument for the 
# function calls
# what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

# print the end result of the add function
print("That becomes: ", what, "Can you do it by hand?")

# print the end result of the add function
print("That becomes: ", result_num, "Can you do it by hand?")