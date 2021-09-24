#!/usr/bin/env python3

# Created by: Michael Zagon
# Created on: Sep 2021
# This program tells a user if they are suited for my grandchild


def main():
    # This function determines if the user is well suited

    # Input
    user_age = input("Enter your age: ")
    print("")

    # Process and Output
    try:
        user_age_number = int(user_age)
        if user_age_number > 40:
            print("You are too old for my grandchild.")
        elif user_age_number < 25:
            print("You are too young for my grandchild.")
        else:
            print("You are well suited for my grandchild.")

    except Exception:
        print("Invalid input.")

    print("\nDone")


if __name__ == "__main__":
    main()
