"""
HIT137 - Group Assignment 1

Group: 42
- Miguel Peachy
- Nick Vecera (S383647)
- John Tijesunimi Ojo
- Alice Lee

Task 1b
Author: Nicholas Vecera
Editor: Alice Lee
"""

# Title for output, \n is just to space it cleanly
print("\n-- Hollow Square Drawer --\n")

# Ask user for square size. Using int because we want whole numbers only.
size = int(input("Enter the size of the square: "))

# Check that the number is positive
if size > 0:
    for i in range(size):
        # Print full row of stars for top and bottom
        if i == 0 or i == size - 1:
            print("* " * size)
        else:
            # Middle rows: one star, space, then one star
            print("*" + "  " * (size - 2) + " *")
else:
    print("Please enter a number greater than 0.")
