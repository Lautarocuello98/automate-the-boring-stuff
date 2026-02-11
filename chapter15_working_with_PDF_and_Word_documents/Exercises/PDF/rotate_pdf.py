import PyPDF2

# open file and read
minutes_file = open('meetingminutes.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(minutes_file)

# set the first page and rotate
page = pdf_reader.getPage(0)
page.rotateClockwise(90)

# open the writer
pdf_writer = PyPDF2.PdfFileWriter()
pdf_writer.addPage(page)

# create the new file and write the page
result_pdf = open('rotatePage.pdf', 'wb')
pdf_writer.write(result_pdf)

# close the files
minutes_file.close()
result_pdf.close()