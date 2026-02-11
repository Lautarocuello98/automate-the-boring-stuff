import os
import win32com.client
import docx

# Get the folder where this script is located
base_dir = os.path.dirname(os.path.abspath(__file__))

# Build absolute paths for the Word and PDF files
word_file_path = os.path.join(base_dir, "your_word_document.docx")
pdf_file_path  = os.path.join(base_dir, "your_pdf_document.pdf")

# Create a Word document in memory
doc = docx.Document()

# Add some example content to the document
doc.add_paragraph("Test document for PDF conversion.")

# Save the Word document to disk
doc.save(word_file_path)

# Word's internal numeric code for saving as PDF
wd_format_pdf = 17

# Start Microsoft Word using COM automation
word_app = win32com.client.Dispatch("Word.Application")

# Keep Word hidden (optional)
word_app.Visible = False

try:
    # Open the Word document using an absolute path
    doc_obj = word_app.Documents.Open(word_file_path)

    # Save the document as a PDF
    doc_obj.SaveAs(pdf_file_path, FileFormat=wd_format_pdf)

    # Close the document
    doc_obj.Close()

finally:
    # Quit Microsoft Word completely
    word_app.Quit()

# Print confirmation messages
print("Saved:", word_file_path)
print("Saved:", pdf_file_path)
