i = 0
numbers = []

# while i < 6:
#     print(f"At the top i is {i}")
#     numbers.append(i)

print(f"At the top i is {i}")

# def count(i, numbers_lenght, inc_number):
#     if i < numbers_lenght:
#         numbers.append(i)
#         i = i + inc_number
#         count(i, numbers_lenght, inc_number)

# count(i, 10, 2)

print(">>>", i)
for i in range(0,10,2):
    print(">>>", i)
    numbers.append(i)

i = i + 1
print("Numbers now: ", numbers)
print(f"At the bottom i is {i}")

print("The numbers: ")

for num in numbers:
    print(num)