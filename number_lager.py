#!/usr/bin/env python3

# Made by Jaydin Madore
# Made on 2022-10-27
# This program tells the user what
def main():
    # Ask the user for the input of number one
    number_one = input("What is number one number ")
    # Ask the user for the input of number two
    number_two = input("What is number two number ")
    print("")

    # Tries casting the user input into an integer.
    try:
        number_one = float(number_one)
        number_two = float(number_two)

    # Restarts program if numbers are not entered
    except ValueError:
        print("You must enter numbers.\n")
        return main()

    # Executed if number one is greater than number two
    if number_one > number_two:
        print(f"{number_one} is greater than {number_two}")

    # Executed if number two is grater than number one
    elif number_one < number_two:
        print(f"{number_two} is greater than {number_one}")

    # Executed if number one and number are equal
    elif number_one == number_two:
        print(f"They are equal")


if __name__ == "__main__":
    main()
    # asks the user if they want to restart after the program has finished
    restart = int(input("Enter 1 if you'd like to restart: "))
    while restart == 1:
        main()
        restart = int(input("Enter 1 if you'd like to restart: "))
