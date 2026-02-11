#! python3
# combine_pdfs.py
# Combines all the PDFs in the current workin directory into a single PDF.

import PyPDF2
import os

# Get all the PDF filenames.
pdf_files = []
for filename in os.listdir('.'):
    if filename.endswith('.pdf') and filename != 'output.pdf':
        pdf_files.append(filename)

pdf_files.sort(key=str.lower)

pdf_writer = PyPDF2.PdfFileWriter()

# Loop through all the PDF files.
for filename in pdf_files:
    pdf_file_obj = open(filename, 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)
    
    # Loop through all the pages.
    for page in range(1, pdf_reader.numPages):
        page_obj = pdf_reader.getPage(page)
        pdf_writer.addPage(page_obj)
        
pdf_file_obj.close()


# Save the resulting PDF to a file.
pdf_ouput = open('output.pdf', 'wb')
pdf_writer.write(pdf_ouput)
pdf_ouput.close()
