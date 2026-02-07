#! python3
# mclip.py - a multi clipboard program.

TEXT = {'agree': """Yes, I agree. That souns fine to me.""",
        'busy': """Sorry, can we do this later this week or next week?""",
        'upsell': """Would you consider making this a monthly donation?"""}

import sys
import pyperclip

if len(sys.argv) < 2:
    print("Usage: python mclip.py [keyphrase] - copy phrase text")
    sys.exit()

keyphrase = sys.argv[1]  #first comand line arg is the keyphrase

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print(f'text for {keyphrase} copied to clipboard.')
else:
    print(f'there is no text for {keyphrase}')