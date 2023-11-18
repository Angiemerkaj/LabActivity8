#!/usr/bin/env python
#Enxhi Merkaj 11/18/2023

#Takes two inputs from a user and print whether their sum is greater than 10, less than 10 or equal to 10.

def compare_sum_to_10():
    # Get input from the user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Calculate the sum
    sum_result = num1 + num2

    # Compare the sum to 10 and print the result
    if sum_result > 10:
        print(f"The sum ({sum_result}) is greater than 10.")
    elif sum_result < 10:
        print(f"The sum ({sum_result}) is less than 10.")
    else:
        print("The sum is equal to 10.")

# Call the function
compare_sum_to_10()
