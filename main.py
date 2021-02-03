#!/usr/bin/env python3

# This is main driver.
def main():
    print("== Ethereum transactions crawler ==")

    w = input("Please enter wallet address:")
    b = input("Please enter block to start from:")

    print("\nSearching for block " + str(b) + " from wallet " + str(w) + "...\n")


if __name__ == "__main__":
    main()
