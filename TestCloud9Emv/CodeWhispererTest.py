# Import necessary packages
from datetime import date

import re

# Function that validates an email address using regex
def validate_email(email):
    if re.match(r"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$", email):
        return True
    else:
        return False

# Main function
def main():
    print("Today's date is: " + date.today().strftime("%B %d, %Y"))

    while True:
        
        email = input("Enter an email address: ")
        
        if validate_email(email):
            print("Valid email address")
            break
        else:
            print("Invalid email address")
            continue

# Call the main function as a script
if __name__ == "__main__":
    main()