
import imaplib
import email
from email.policy import default

# --- CONFIG (edit these) ---
IMAP_HOST = "imap.gmail.com"
IMAP_PORT = 993
EMAIL_ADDRESS = "tu_email@gmail.com"
APP_PASSWORD = "tu_app_password"  # Gmail usually needs an App Password (not your normal password)

# 1) Connect to the IMAP server using SSL
imap = imaplib.IMAP4_SSL(IMAP_HOST, IMAP_PORT)

# 2) Login
imap.login(EMAIL_ADDRESS, APP_PASSWORD)

# 3) Select the mailbox (INBOX)
# readonly=False allows us to mark emails as read
imap.select("INBOX", readonly=False)

# 4) Search for unread emails (UNSEEN)
status, data = imap.search(None, "UNSEEN")
email_ids = data[0].split()

print("Unread emails found:", len(email_ids))

if not email_ids:
    # No unread emails, just logout
    imap.logout()
    raise SystemExit

# Pick the newest unread email (last id in the list)
eid = email_ids[-1]

# 5) Fetch the full raw email (RFC822)
status, msg_data = imap.fetch(eid, "(RFC822)")
raw_email = msg_data[0][1]

# Parse the raw email into an EmailMessage object
msg = email.message_from_bytes(raw_email, policy=default)

# Print basic headers
print("\n--- HEADERS ---")
print("Subject:", msg.get("subject"))
print("From:", msg.get("from"))
print("To:", msg.get("to"))

# 6) Get the body (prefer text/plain; fallback to text/html)
body = ""
if msg.is_multipart():
    for part in msg.walk():
        # Skip attachments
        if part.get_content_disposition() == "attachment":
            continue

        # Prefer plain text
        if part.get_content_type() == "text/plain":
            body = part.get_content()
            break

    # If no text/plain found, try HTML
    if not body:
        for part in msg.walk():
            if part.get_content_disposition() == "attachment":
                continue
            if part.get_content_type() == "text/html":
                body = part.get_content()
                break
else:
    # Single-part email
    body = msg.get_content()

print("\n--- BODY ---")
print(body.strip() if body else "(no body found)")

# 7) Mark the email as read by adding the \Seen flag
imap.store(eid, "+FLAGS", "\\Seen")
print("\nMarked as read:", eid.decode())

# 8) Logout
imap.logout()
print("Logged out.")
