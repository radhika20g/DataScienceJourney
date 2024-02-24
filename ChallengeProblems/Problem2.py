#Problem Statement - Create a Python program that prompts the user to enter positive numbers continuously. The program should use a while loop to collect input data until the user enters a non-positive number. Implement simple data validation to ensure entered values are valid positive numbers. Finally, output the list of positive numbers entered by the user. The objective is to create an interactive and error-tolerant program for collecting and handling user input.

numbers = []

while True:
    num = input("Enter a +ve (Enter a -ve number if you want to stop): ")
    if num.replace('.','',1).isdigit() and float(num) > 0:
        numbers.append(float(num))
    elif num.replace('-', '', 1).isdigit() and float(num) <= 0:
        break
    else:
        print("Invalid Input. Please enter a valid +ve number!")

if numbers:
    print(f"You have entered the following numbers: {numbers}.")
else:
    print("No positive numbers were entered.")