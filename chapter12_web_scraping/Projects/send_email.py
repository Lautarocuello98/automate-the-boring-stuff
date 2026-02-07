import argparse
import os
import smtplib
from email.message import EmailMessage
from pathlib import Path

# This script allows you to **send an email from the terminal using SMTP (Gmail), taking the recipient, 
# subject, and message from command-line arguments or from a file, and using credentials defined
# in environment variables**.



# Send one email using SMTP over SSL (Gmail)
def send_email_smtp(to_addr: str, subject: str, body: str) -> None:
    user = os.environ.get('EMAIL_USER')
    password = os.environ.get('EMAIL_PASS')

    # 1) Validate credentials
    if not user or not password:
        raise SystemExit(
            "Missing EMAIL_USER / EMAIL_PASS.\n"
            "Example (PowerShell):\n"
            "   $env:EMAIL_USER='youraccount@gmail.com'\n"
            "   $env:EMAIL_PASS='your_app_password'\n"
        )

    # 2) Build the email
    msg = EmailMessage()
    msg['From'] = user
    msg['To'] = to_addr
    msg['Subject'] = subject
    msg.set_content(body)

    # 3) Connect to the Gmail SMTP server and send
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(user, password)
        smtp.send_message(msg)


def main() -> None:
    # 4) Define command line arguments
    parser = argparse.ArgumentParser(
        description="Send an email from the terminal using SMTP."
    )

    # Positional: recipient
    parser.add_argument("to", help="Recipient email address")

    # Optional positional: text (if --file is not used)
    parser.add_argument(
        "text",
        nargs="?",
        default=None,
        help="Message text (optional if --file is used)"
    )

    # Optional: subject
    parser.add_argument(
        "--subject",
        default="Notification",
        help="Email subject"
    )

    # Optional: read body from file
    parser.add_argument(
        "--file",
        type=str,
        default=None,
        help="Path to a .txt file to use as the email body"
    )

    args = parser.parse_args()

    # 5) Choose where the body comes from: file or text
    if args.file:
        body = Path(args.file).read_text(encoding="utf-8")
    elif args.text is not None:
        body = args.text
    else:
        raise SystemExit("You must provide text or use --file.")

    # 6) Send email
    send_email_smtp(args.to, args.subject, body)
    print("Email sent.")


if __name__ == "__main__":
    main()
