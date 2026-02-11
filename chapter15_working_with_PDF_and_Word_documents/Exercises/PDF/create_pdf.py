import PyPDF2

# open both PDFs in bynary read mode
pdf_file1 = open('meetingminutes.pdf', 'rb')
pdf_file2 = open('meetingminutes.pdf', 'rb')

# create readers for both PDFs
pdf1_reader = PyPDF2.PdfFileReader(pdf_file1)
pdf2_reader = PyPDF2.PdfFileReader(pdf_file2)

# create a writer for the output PDF 
pdf_writer = PyPDF2.PdfFileWriter()

# Copy all pages from the first PDF
for page_num in range(pdf1_reader.numPages):
    page_obj = pdf1_reader.getPage(page_num)
    pdf_writer.addPage(page_obj)

# copy all pages from the second PDF
for page_num in range(pdf2_reader.numPages):
    page_obj = pdf2_reader.getPage(page_num)
    pdf_writer.addPage(page_obj)

# write the combined PDF to disk
pdf_output_file = open('combinedminutes.pdf', 'wb')
pdf_writer.write(pdf_output_file)

# close output and input files
pdf_output_file.close()
pdf_file2.close()
pdf_file1.close()