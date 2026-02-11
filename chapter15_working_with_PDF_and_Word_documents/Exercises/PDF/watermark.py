import PyPDF2

# Open the original PDF in binary read mode
pdfReader = open('meetingminutes.pdf', 'rb')

# Create a reader object to work with the PDF
minutes = PyPDF2.PdfFileReader(pdfReader)

# Get the first page of the original PDF
minutes_first_page = minutes.getPage(0)


# Open the watermark PDF
watermarkReader = open('watermark.pdf', 'rb')

# Create a reader object for the watermark
watermark = PyPDF2.PdfFileReader(watermarkReader)

# Get the first page of the watermark PDF
watermark_first_page = watermark.getPage(0)


# Merge the watermark page onto the first page of the original PDF
minutes_first_page.mergePage(watermark_first_page)


# Create a writer object to build the new PDF
pdf_writer = PyPDF2.PdfFileWriter()

# Add the modified first page (with watermark)
pdf_writer.addPage(minutes_first_page)


# Add the rest of the pages from the original PDF unchanged
for page_num in range(1, minutes.numPages):
    page_obj = minutes.getPage(page_num)
    pdf_writer.addPage(page_obj)


# Open a new file in binary write mode to save the result
result_file = open('waterMarkedCover.pdf', 'wb')

# Write the new PDF to disk
pdf_writer.write(result_file)


# Close all opened files to free resources
watermarkReader.close()
pdfReader.close()
result_file.close()
