#! python3
# search_pypi.py - opens the PyPI search page

import sys
import webbrowser

query = " ".join(sys.argv[1:]).strip()
if not query:
    print("usage: python search_pypi.py <search terms>")
    sys.exit(1)

url = f"https://pypi.org/search/?q={query}"
print(f"Opening {url}")
webbrowser.open(url)