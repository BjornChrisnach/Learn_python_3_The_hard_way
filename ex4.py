# Assigns 100 into cars variable
cars = 100
# Assigns 4.0 into space_in_a_car variable
space_in_a_car = 4.0
# Assigns 30 into drivers variable
drivers = 30
# Assigns 90 into passengers variable
passengers = 90
# Assigns the substraction between the cars and drivers variable
cars_not_driven = cars - drivers
# Assigns drivers amount into cars_driven variable
cars_driven = drivers
# Assigns the multiplication of cars_driven and space_in_a_car variable, to the carpool_capacity variable
carpool_capacity = cars_driven * space_in_a_car
# Assigns the division between passengers and cars_driven into the average_passengers_per-car variable
average_passengers_per_car = passengers / cars_driven

# prints how many cars there are available
print("There are", cars, "cars available.")
# prints how many drivers there are available
print("There are only", drivers, "drivers available.")
# prints how many empty cars there are
print("There will be", cars_not_driven, "empty cars today.")
# prints how many passengers can be transported
print("We can transport", carpool_capacity, "people today.")
# prints how many passengers are carpooling
print("We have", passengers, "to carpool today.")
# prints out how many passengers are in each car
print("We need to put about", average_passengers_per_car, "in each car.")

# Study drills
# car_pool_capacity, name is not defined. it's carpool_capacity
