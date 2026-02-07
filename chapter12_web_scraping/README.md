# Chapter 12 – Web Scraping 🌐

Scripts from **Chapter 12: Web Scraping**.

## Topics Covered
- HTTP requests
- Web scraping concepts
- HTML parsing
- Extracting data from websites
- BeautifulSoup (bs4)
- Selenium
- Sending email notifications (SMTP)

## Goal
Automate the collection of data from web pages and trigger automated actions such as notifications.

## Notes
Web scraping introduces interaction with external data sources and basic browser automation.

For the **Command Line Emailer** exercise, I implemented the solution using **SMTP (smtplib)** instead of Selenium.  
This approach is more reliable in modern environments because many email providers block automated browser logins with CAPTCHA and two-factor authentication.

## Projects
download_xkcd.py (Downloads every single XKCD comic.)

send_email.py (Sends an email from the terminal using Gmail SMTP, with the message provided as arguments or from a file.)

images_downloader.py (Downloads all images from a given webpage URL)