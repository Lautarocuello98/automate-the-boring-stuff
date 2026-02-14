#! python3
# auto_unsubscriber.py
# Logs into an email account, finds unsubscribe links, and opens them.

import imapclient
import pyzmail
import webbrowser
import bs4

# Login to email account
imap_obj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
imap_obj.login('lautaro123@gmail.com', 'password')

# Select inbox
imap_obj.select_folder('INBOX', readonly=True)

# Search for emails that contain the word "unsubscribe"
uids = imap_obj.search(['TEXT', 'unsubscribe'])

print(f'Found {len(uids)} messages with "unsubscribe".')

links = []

# Go through each email
for uid in uids:
    raw_message = imap_obj.fetch([uid], ['BODY[]', 'FLAGS'])
    message = pyzmail.PyzMessage.factory(raw_message[uid][b'BODY[]'])

    # Get the HTML part of the email
    if message.html_part is None:
        continue

    html = message.html_part.get_payload().decode(message.html_part.charset)

    # Parse HTML with BeautifulSoup
    soup = bs4.BeautifulSoup(html, 'html.parser')

    # Find all links
    for link in soup.find_all('a'):
        href = link.get('href')
        if href and 'unsubscribe' in href.lower():
            links.append(href)

imap_obj.logout()

# Open links in browser
for link in links:
    print('Opening:', link)
    webbrowser.open(link)
