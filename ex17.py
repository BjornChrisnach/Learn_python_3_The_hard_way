from sys import argv
from os.path import exists

# unpack the rgvs into the variables
script, from_file, to_file = argv

# print origin and destination file
print(f"Copying from {from_file} to {to_file}")

# we could do these two on one line, how?
# create the file object for the origin file
in_file = open(from_file)
# read the entire file
indata = in_file.read()

# print the lenght of the origin file
# print(f"The input file is {len(indata)} bytes long")

# print a test to see if the output file exists
# print(f"Does the output file exist? {exists(to_file)}")
# Give the user the decision to abort or to go ahead to copy the file
# print("Ready, hit RETURN to continue, CTRL-C to abort")
# wait for user input
# input()

# create the file object for the output file, and open mode to write
out_file = open(to_file, 'w')
# write the entire file to the output file
out_file.write(indata)

# print the status for the user
print("Alright, all done.")

# close both open files
out_file.close()
in_file.close()