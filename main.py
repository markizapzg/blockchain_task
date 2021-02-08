#!/usr/bin/env python3

# This is main driver.
def main():
    print("== Ethereum transactions crawler ==")

    w = input("Please enter wallet address:")
    b = input("Please enter block to start from:")

    if len(w) == 42:
        print("Wallet address is correct.")
    else:
    	print("Try again with correct address")

    if int(b) > 0:
        print("\nSearching for block " + str(b) +
                  " from wallet " + str(w) + "...\n")
    else:
        print("Block number can't be less than 0.")
        
if __name__ == "__main__":
    main()
