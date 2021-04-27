# put placeholders inside of the formatter string
formatter = "{} {} {} {}"

# print the formatted string with the given arguments: 1, 2, 3, 4
print(formatter.format(1, 2, 3, 4))
# print the formatted string with the given arguments: "one", "two", "three", "four"
print(formatter.format("one", "two", "three", "four"))
# print the formatted string with the given arguments: True, False, False, True
print(formatter.format(True, False, False, True))
# print the formatted string with the given arguments: the formatter 4 times
print(formatter.format(formatter, formatter, formatter, formatter))
# print the formatted string with the given arguments: the 4 strings
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
    ))