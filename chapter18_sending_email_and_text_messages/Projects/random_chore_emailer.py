#! python3
# random_chore_emailer.py
# Assigns a random chore to each person and emails them the result.

import random
import smtplib
import sys

# List of people with their emails
peoples = [
    {"name": "liliana", "email": "liliana@gmail.com"},
    {"name": "lautaro", "email": "lautaro@gmail.com"},
    {"name": "maria", "email": "maria@gmail.com"},
    {"name": "agustin", "email": "agustin@gmail.com"}
]

# List of chores (must be at least as many chores as people)
chores = ['dishes', 'bathroom', 'vacuum', 'walk dog']

# Connect to the SMTP server (Gmail)
smtp_obj = smtplib.SMTP("smtp.gmail.com", 587)
smtp_obj.ehlo()        # Identify with the mail server
smtp_obj.starttls()    # Encrypt the connection

# Login using the email password passed from command line
smtp_obj.login("my_email@gmail.com", sys.argv[1])


def assign_chores(peoples: list[dict], chores: list[str]) -> list[dict]:
    # Ensure there are enough chores for everyone
    if len(chores) < len(peoples):
        raise ValueError("Not enough chores for the number of people.")

    # Copy the chores list so we can remove items safely
    remaining = chores[:]
    assignments: list[dict] = []

    # Assign one random chore to each person (no repeats)
    for person in peoples:
        chore = random.choice(remaining)
        remaining.remove(chore)

        # Store the result
        assignments.append({
            "name": person["name"],
            "email": person["email"],
            "chore": chore
        })

    return assignments


def main() -> None:
    # Generate assignments
    assignments = assign_chores(peoples, chores)

    # Send one email per person
    for people in assignments:

        # Build email message (Subject must be first line)
        body = (
            "Subject: Chore assignment\n\n"
            f"Hi {people['name']},\n\n"
            f"Your chore for this week is: {people['chore']}\n\n"
            "Thanks!"
        )

        # Send the email
        smtp_obj.sendmail("my_email@gmail.com", people["email"], body)


if __name__ == "__main__":
    main()

    # Close the connection to the SMTP server
    smtp_obj.quit()
