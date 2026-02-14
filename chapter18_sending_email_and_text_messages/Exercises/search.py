import ezgmail

threads = ezgmail.search("RoboCop")
threads_unread = ezgmail.search("label:unread")
threads_from = ezgmail.search("from:example@gmail.com")
threads_invoice = ezgmail.search("subject:invoice")
threads_attachment = ezgmail.search("has:attachment")

# how many results
print(len(threads))
print(len(threads_from))

# show summaries
ezgmail.summary(threads)
ezgmail.summary(threads_from)
