"""Gets the user's name and age and calculates their approximate birth year."""

Input:
    User's name as a string.
    User's age as an integer.


Process:
    Subtract the user's age from the current year to find the birth year.

Output:
    A message showing the user's name and approximate birth year.
    
Typical usage example:
    What is your name? Ruby
    How old are you? 31
    Hello Ruby! You were born in 1995.
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

    birth_year = CURRENT_YEAR - age



    # Output personalized message with user's name and birth year.
print(f"Hello {name}! You were born in {birth_year}.")

# === Main Guard ===
if __name__ == "__main__":
    main()


# === References ===
