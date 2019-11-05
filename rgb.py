#!/usr/bin/env python3

# Created by: Matsuru Hoshi
# Created on: Sept 2019
# This is program prints all rgb combinatiosns


def main():
    # funciton adds positive numbers

    # variables
    red = 0
    green = 0
    blue = 0

    # Welcome statement
    print("Hi, I’ll print all possible RGB combinations")
    # input
    input("Press Enter to start.")
    
    # process
    for red in range(255):
        for green in range(255):
            for blue in range(255):
                print("RGB: (" + str(red) + ", " + str(green) + ", " +
                      str(blue) + ")")


if __name__ == "__main__":
    main()
