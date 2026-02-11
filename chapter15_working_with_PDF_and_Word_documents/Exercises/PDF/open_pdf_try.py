import PyPDF2

# open pdf
pdf_file_obj = open('meetingminutes.pdf', 'rb')

# read pdf
pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)

# print how many pages
print(pdf_reader.numPages)

# get the first page
page_obj = pdf_reader.getPage(0)

# extract text and print
print(page_obj.extractText())

# close file
pdf_file_obj.close()