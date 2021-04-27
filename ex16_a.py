from sys import argv

# unpack arguments to the given variables
script, filename = argv

# store the return value from the open(filename) command in txt
txt = open(filename)

# print the entire contents of the file
print(txt.read())

# close the opened file
txt.close()