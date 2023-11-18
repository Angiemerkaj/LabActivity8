#!/usr/bin/env python
#Enxhi Merkaj 11/18/2023

#Takes a list and prints if the value 5 is in that list
def get_list_from_user():
    # Get input from the user, assuming space-separated numbers
    input_string = input("Enter a list of numbers separated by spaces: ")

    # Convert the input string into a list of integers
    try:
        number_list = [int(x) for x in input_string.split()]
        return number_list
    except ValueError:
        print("Invalid input. Please enter valid numbers separated by spaces.")
        return []

user_numbers = get_list_from_user()
print("User input:", user_numbers)

#A function to check whether 5 is in the list
def check_for_5(input_list):
    if 5 in input_list:
        print("The value 5 is in the list.")
    else:
        print("The value 5 is not in the list.")
#Call the function
check_for_5(user_numbers)
