# brute_force_pdf_password.py
# Try passwords from a dictionary file to unlock an encrypted PDF.

import PyPDF2

# Open the encrypted PDF in read-binary mode
pdf_file = open("encrypted.pdf", "rb")
pdf_reader = PyPDF2.PdfFileReader(pdf_file)

# Load all candidate passwords (one per line)
with open("dictionary.txt") as f:
    words = f.read().splitlines()

# Try each word in original, upper, and lower case
for word in words:
    for attempt in (word, word.upper(), word.lower()):
        
        # decrypt() returns True/1 if the password is correct
        if pdf_reader.decrypt(attempt):
            print("Password found:", attempt)
            pdf_file.close()
            exit()

# If no password worked
print("Password not found.")
pdf_file.close()
