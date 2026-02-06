#! python3
# extending_multi_clipboard.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe extending_multi_clipboard.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe extending_multi_clipboard.pyw <keyword> - Loads keyword to clipboard.
#        py.exe extending_multi_clipboard.pyw list - Loads all keywords to clipboard.
#        py.exe extending_multi_clipboard.pyw deleteall - delete all keywords.
#        py.exe extending_multi_clipboard.pyw <keyword> - Delete keyword.

import shelve
import pyperclip
import sys

mcbShelf = shelve.open('mcb')   

# save clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()

elif len(sys.argv) == 2:
    # list keywords and load content
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))

    elif sys.argv[1].lower() == 'deletall':
        mcbShelf.clear()

    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
    
    elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
        if sys.argv[2] in mcbShelf:
            del mcbShelf[sys.argv[2]]

else:
    print("incorrect usage")
    print("usage: py.exe extending_multi_clipboard.pyw save <keyword> - Saves clipboard to keyword.")
    print("usage: py.exe extending_multi_clipboard.pyw <keyword> - Loads keyword to clipboard.")
    print("usage: py.exe extending_multi_clipboard.pyw deleteall - Delete all keyword to clipboard.")
    print("usage: py.exe extending_multi_clipboard.pyw list - Loads all keywords.")
    print("usage: py.exe extending_multi_clipboard.pyw <keyword> - Delete keyword")

mcbShelf.close()