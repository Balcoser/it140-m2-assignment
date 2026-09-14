"""This program asks for a name and age and calculates the birth year.

Input:
    Name - string entered by the user.
    Age - integer entered by the user.
    Current year - integer provided by the system.

Process:
    Calculate the birth year by subtracting the user's age from the current year.

Output:
    personalized message with the user's name and birth year - string displayed in the console.

Typical usage example:
    What is your name? Alex
    How old are you? 24
    Hello Alex! You were born in 2001.
"""

# === Imports ===
from datetime import date

# === Constants ===
CURRENT_YEAR = date.today().year  # Get current year from system as integer


# === Main Function ===
def main() -> None:
    """Run the name-age program."""

    # Get user input.
    name = input("What is your name? ")
    age = int(input("How old are you? "))

    # Calculate user's approximate birth year.
    birth_year = CURRENT_YEAR - age

    # Output personalized message with user's name and birth year.
    print(f"Hello {name}! You were born in {birth_year}.



# === Main Guard ===
if __name__ == "__main__":
    main()


# === References ===
# TODO: Replace with an APA-style reference for a source you used, or delete.
# TODO: Replace with another APA-style reference, or delete this TODO line.
