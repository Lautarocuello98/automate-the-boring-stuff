import docx

# Function that reads a Word document and returns all its text
def getText(filename):

    # Open the Word document
    doc = docx.Document(filename)

    # Create a list to store the text of each paragraph
    fullText = []

    # Loop through all paragraphs in the document
    for para in doc.paragraphs:

        # Append the text of each paragraph to the list
        fullText.append(para.text)

    # Join all paragraphs into a single string separated by line breaks
    return '\n'.join(fullText)

print(getText('demo.docx'))