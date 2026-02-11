import PyPDF2

# Open the encrypted PDF
pdf_file = open('encrypted.pdf', 'rb')

# Create a PDF reader
pdf_reader = PyPDF2.PdfFileReader(pdf_file)

# Check if the PDF is encrypted (True or False)
print(pdf_reader.isEncrypted)

# Decrypt the PDF using the password 
pdf_reader.decrypt('rosebud')

# Get the first page of the PDF
page = pdf_reader.getPage(0)

# Extract and print the text from the page
print(page.extractText())

# Close the file
pdf_file.close()
