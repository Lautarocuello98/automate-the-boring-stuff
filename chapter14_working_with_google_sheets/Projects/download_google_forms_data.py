# download_google_forms_data.py
# Retrieve emails from Google Sheets, clean them, and display results.

import ezsheets

SPREADSHEET_ID = "1Q5SNOADgOP26Z5eyvia-3HTmx5m45ssCaDa1hH2wZ3M"

ss = ezsheets.Spreadsheet(SPREADSHEET_ID)
sheet = ss[0]

# get emails from column c and skip header
emails = sheet.getColumn(3)[1:]

clean_emails = []

for email in emails:
    # Skip None values
    if email is None:
        continue

    # Remove spaces at beginning and end
    email = email.strip()

    # Skip empty strings
    if email == "":
        continue

    clean_emails.append(email)

emails = clean_emails

print(emails)
