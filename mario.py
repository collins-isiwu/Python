'''a python program to print a left aligned half pyramid'''
from cs50 import get_int

# prompt user for the height of half pyramid
n = get_int("enter height of pyramid?: ")

# re-prompt the user again if the int is't a positive integer between 1 and 8, inclusive
while n < 1 or n > 8:
    print("invalid")
    n = int(input("enter height of pyramid?: "))

for row in range(n):
    for column in range(n):  # to make a grid
        if column < n - (row + 1):  # to flip the grid
            print(" ", end="")   # to print space 
        else:
            print("#", end="")   # to print #
    print()
