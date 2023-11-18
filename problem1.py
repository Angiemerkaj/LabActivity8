#!/usr/bin/env python
#Enxhi Merkaj 11/18/2023

#Takes two inputs from a user and print whether they are equal or not

def compare_input():
#Prompt the user for input

    input1 = input("Enter the first value: ")
    input2 = input("Enter the second value: ")

#Compare the inputs
    if input1 == input2:
         print("The inputs are equal!")
    else:
        print("The inputs are not equal!")

#Call the function
compare_input()
