from sys import argv

# unpack the command line input
script, user_name, user_age = argv
# prompt = '> '
prompt = f'{script} ({user_name})'

# print the formatted string, with user_name and age. and the script name.
print(f"Hi {user_name}, your age is {user_age}. I'm the {script} script.")
# print the user input stuff
print("I'd like to ask you a few questions.")
# Ask a question, with a formatted string, with user_name
print(f"Do you like me {user_name}?")
# show the prompt for input and store it in likes
likes = input(prompt)

# print the formatted string with user_name
print(f"Where do you live {user_name}?")
# show the prompt for input and store it in lives
lives = input(prompt)

# print the question, with formatted string, with user_name data
print(f"How old are you {user_name}?")
# catch the possible error here or below
# age = input(prompt)
age = int(input(prompt))

# catch the possible error here or above
# print(f"You're {int(age)}. What kind of computer do you have?")
# it's better to catch the error at the first available time, so above
print(f"You're {age}. What kind of computer do you have?")
# show the prompt for input and store in computer
computer = input(prompt)

# print the formatted or f-string with likes, lives and computer
print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer nice.
""")