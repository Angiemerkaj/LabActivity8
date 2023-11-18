#!/usr/bin/env python
#Enxhi Merkaj 11/18/2023

#Takes a year as a parameter and returns True if the year is a leap year, False if it is otherwise.

def is_leap_year(year):
    # Check if the year is evenly divisible by 4
    if year % 4 == 0:
        # If the year is evenly divisible by 100
        if year % 100 == 0:
            # If the year is also evenly divisible by 400, it's a leap year
            if year % 400 == 0:
                return True
            else:
                return False
        # If the year is not divisible by 100, it's a leap year
        else:
            return True
    # If the year is not divisible by 4, it's not a leap year
    else:
        return False

# Example usage:
year_to_check = int(input("Enter a year: "))
result = is_leap_year(year_to_check)

if result:
    print(f"{year_to_check} is a leap year.")
else:
    print(f"{year_to_check} is not a leap year.")
