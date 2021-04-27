from sys import argv

# Unpack the argv to the variables
script, filename = argv

# print the f-string with filename
print(f"We're going to erase {filename}.")
# print instructions to cancel
print("If you don't want that, hit CTRL-C (^c).")
# print instructions how to proceed
print("If you do want that, hit RETURN.")

# Wait for the user's decision
input("?")

# print that we are going to open the file
print("Opening the file...")
# open the file for writing, save the file object in target
target = open(filename, 'w')
# print that you are truncating the file
print("Truncate the file. Goodbye!")
# execute the truncate command
target.truncate()

# print that you are going to ask input
print("Now I'm going to ask you for three lines.")

# store first input in Line1
Line1 = input("Line 1: ")
# store second input in Line2
Line2 = input("Line 2: ")
# store third input in Line3
Line3 = input("Line 3: ")

# print to inform the user that you are going to write to the file
print("I'm going to write these to the file.")

prepared_string = (f"{Line1}\n{Line2}\n{Line3}\n")
target.write(prepared_string)
# # execute the write command for Line1
# target.write(Line1)
# # write a newline statement to the file, to write on the next line
# target.write("\n")
# # execute the write command for line2
# target.write(Line2)
# # write a newline statement to the file, to write on the next line
# target.write("\n")
# # execute the write command for Line3
# target.write(Line3)
# # write a newline statement to the file, to write on the next line
# target.write("\n")

# print the final text for the user
print("And finally. We close it.")
# execute the close command for the file
target.close()
