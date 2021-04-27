from sys import argv

# unpack argv into the variables
script, input_file = argv

# a function that prints the whole file
def print_all(f):
    print(f.read())

# put the pointer back to the beginning of the file
def rewind(f):
    f.seek(0)

# a function that prints a line from a given file
def print_a_line(line_count, f):
    print(line_count, f.readline())

# Put the file object in the current_file
current_file = open(input_file)

# print what will be printed first
print("First let's print the whole file:\n")

# call a function, to print the whole input from the file
print_all(current_file)

# print that we have to put the pointer back to the beginning of the file
print("Now let's rewind, kind of like a tape.")

# call a function, to put the pointer back to the beginning of the file
rewind(current_file)

# print what is to be printed next
print("Let's print three lines:")

# set the line numbering to 1
current_line = 1
# call a function, to print the first line with line numbering 1
print_a_line(current_line, current_file)

# set the line numbering to 2
# current_line = current_line + 1
current_line += 1
# call a function, to print the second line with line numbering 2
print_a_line(current_line, current_file)

# set the third numbering to 3
# current_line = current_line + 1
current_line += 1
# call a function, to print the third line with line numbering 3
print_a_line(current_line, current_file)