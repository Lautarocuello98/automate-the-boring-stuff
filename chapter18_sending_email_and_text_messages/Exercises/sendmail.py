import ezgmail

ezgmail.send(
    "mail_recipient@gmail.com",
    "Daily report",
    "Body of the mail. Attached file.",
    ["report.xlsx"],
    cc="friend@example.com"
)