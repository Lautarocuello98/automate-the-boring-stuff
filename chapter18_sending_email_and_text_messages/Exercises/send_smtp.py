import smtplib  # Import the library used to send emails via SMTP


# Create an SMTP connection object.
# "smtp.gmail.com" is Gmail's SMTP server.
# 587 is the standard port for TLS encryption.
smtpObj = smtplib.SMTP("smtp.gmail.com", 587)


# Identify ourselves to the SMTP server.
# This step starts communication between client and server.
smtpObj.ehlo()


# Start TLS encryption to secure the connection.
# This protects your login credentials and email content.
smtpObj.starttls()


# Log in to the email account.
# Replace with your real email and password or an app password.
smtpObj.login("your_email@gmail.com", "your_password")


# Send an email.
# First argument: sender address
# Second argument: recipient address
# Third argument: full message (must include Subject and body separated by a blank line)
smtpObj.sendmail(
    "your_email@gmail.com",
    "recipient@gmail.com",
    "Subject: Hello\n\nThis is the body of the message"
)


# Close the connection to the SMTP server.
smtpObj.quit()
