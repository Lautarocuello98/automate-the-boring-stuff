import PyPDF2

pdfFile = open('meetingminutes.pdf','rb')
pdfreader = PyPDF2.PdfFileReader(pdfFile)

pdf_writer = PyPDF2.PdfFileWriter()

# Loop through all pages in the original PDF
for page_num in range(pdfreader.numPages):
    # Add each page to the writer
    pdf_writer.addPage(pdfreader.getPage(page_num))

# Encrypt the new PDF with a password
pdf_writer.encrypt('swordfish')

result_pdf = open('encryptedminutes.pdf', 'wb')
pdf_writer.write(result_pdf)

pdfFile.close()
result_pdf.close()