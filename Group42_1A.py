'''
HIT137 - Group Assignment 1

Group: 42
- Miguel Peachy (S384873) 
- Nick Vecera (S383647)
- John Tijesunimi Ojo (S389743)
- Alice Lee (S394431)

Task 1A
Author's: - Nicholas Vecera
          -  
    Editor's: -Alice Lee
              - 

            
'''

# Display the ttle, i used \n for a paragraph break to tidy how it is displayed.
print("\n-- Triangle Checker -- \n ")
#I add try-except blocks to make safe programming
try:
# Ask the user for 3 numbers, float is used to allow decimal values. 
    a = float(input("Enter your 1st number: "))
    b = float(input("Enter your 2nd number: "))
    c = float(input("Enter your 3rd number: "))

# Check if the numbers make a triangle (triangle inequality rule)
    if a + b > c and b + c > a and a + c > b:
    # Yep, it's a triangle 
        print(f"\nThe values: {a}, {b}, and {c} \n\ncan form a triangle.") # f string inserts the variable values into the sentence directly, \n is used again for tidy spacing.
 
    else:
    # Nope, can't form a triangle
        print(f"\nThe values {a}, {b}, and {c} \n\ncannot form a triangle.")
except Exception as e:
    print(e)
