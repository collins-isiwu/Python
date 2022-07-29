# the greedy theory

from cs50 import get_float

change = get_float("change owned: ")

while change < 0:
    change = get_float("change owned: ")

cents = round(change * 100)

# create variable for the amount still owned
reminder1 = 0
reminder2 = 0
reminder3 = 0

# how many coins used so far variable
coinused1 = 0
coinused2 = 0
coinused3 = 0
coinused4 = 0

if cents % 25 == 0:
    coinused1 = cents / 25
elif cents % 25 != 0:
    reminder1 = cents % 25
    coinused1 = int(cents / 25)
    
if reminder1 % 10 == 0:
    coinused2 = reminder1 / 10
elif reminder1 % 10 != 0:
    reminder2 = reminder1 % 10
    coinused2 = int(reminder1 / 10)
    
if reminder2 % 5 == 0:
    coinused3 = reminder2 / 5
elif reminder2 % 5 != 0:
    reminder3 = reminder2 % 5
    coinused3 = int(reminder2 / 5)
    
if reminder3 % 1 == 0:
    coinused4 = int(reminder3 / 1)
    

print(f"number of coin used: {coinused1 + coinused2 + coinused3 + coinused4}")
