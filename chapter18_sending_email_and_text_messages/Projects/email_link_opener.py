#! python3
# email_link_opener.py
# Checks an email account every 15 minutes for new messages with a special subject.
# If it finds one, it extracts the first URL from the email body and opens it in a browser.
# Then it marks the email as read so it won't run again.

import re
import time
import webbrowser
from imapclient import IMAPClient
import pyzmail

# ---------------- CONFIG ----------------
IMAP_HOST = "imap.gmail.com"
EMAIL_ADDRESS = "YOUR_EMAIL@gmail.com"
EMAIL_PASSWORD = "YOUR_APP_PASSWORD"  # Use an app password (Gmail), not your normal password.

SUBJECT_KEYWORD = "OPENLINK"  # The email subject must contain this word.
CHECK_EVERY_SECONDS = 15 * 60  # 15 minutes
# ----------------------------------------


def find_first_url(text: str) -> str | None:
    # Simple URL regex: finds the first http(s) link.
    m = re.search(r"https?://\S+", text)
    if not m:
        return None
    # Strip trailing punctuation that often sticks to URLs in emails.
    return m.group(0).rstrip(").,;!\"'")


def get_email_text(message) -> str:
    # Prefer plain text; if not available, fall back to HTML.
    if message.text_part:
        return message.text_part.get_payload().decode(message.text_part.charset or "utf-8", errors="replace")
    if message.html_part:
        return message.html_part.get_payload().decode(message.html_part.charset or "utf-8", errors="replace")
    return ""


while True:
    with IMAPClient(IMAP_HOST, ssl=True) as imap:
        imap.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        imap.select_folder("INBOX", readonly=False)

        # Search for unread messages that contain the subject keyword.
        uids = imap.search(["UNSEEN", "SUBJECT", SUBJECT_KEYWORD])

        if uids:
            raw_messages = imap.fetch(uids, ["BODY[]"])

            for uid in uids:
                message = pyzmail.PyzMessage.factory(raw_messages[uid][b"BODY[]"])

                subject = message.get_subject() or ""
                body_text = get_email_text(message)

                url = find_first_url(body_text)

                if url:
                    print(f"Opening: {url}")
                    webbrowser.open(url)
                else:
                    print(f"No URL found in email subject: {subject}")

                # Mark as read so it doesn't repeat next cycle.
                imap.add_flags(uid, [b"\\Seen"])

        imap.logout()

    time.sleep(CHECK_EVERY_SECONDS)