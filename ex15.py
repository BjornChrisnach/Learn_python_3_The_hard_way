from sys import argv

# unpack arguments to the given variables
script, filename = argv

# store the return value from the open(filename) command in txt
txt = open(filename)

# print the f-string, with filename
print(f"Here's your file {filename}:")
# print the entire contents of the file
print(txt.read())

# close the opened file
txt.close()

# Ask to enter the filename again
print("Type the filename again:")
# store the filename into file_again, show the > prompt at input
file_again = input("> ")

# store the return value from the open(filename) command in txt_again
txt_again = open(file_again)

# print the entire contents of the file again
print(txt_again.read())

# close the opened file
txt_again.close()