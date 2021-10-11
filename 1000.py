# !/user/bin/env python3

# Created by Trent Hodgins
# Created on 10/06/2021
# This is the RGB program
# This program displays all numbers from 1000 to 2000


def main():
    # this function does addition math

    # process and output
    counter = 0

    for counter in range(1000, 2001):
        if counter % 5 == 0:
            print("")
            print(counter, end=" ")
        else:
            print("{0} ".format(counter), end="")

    print("\nDone")


if __name__ == "__main__":
    main()
