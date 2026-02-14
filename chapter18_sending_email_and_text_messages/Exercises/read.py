import ezgmail

threads = ezgmail.unread()


print("Unread threads:", len(threads))

for thread in threads:
    for message in thread.messages:
        print("From:", message.sender)
        print("Subject:", message.subject)
        print("Body:", message.body)
        print("-" * 40)


print("First sender:", threads[0].messages[0].sender)
print("First subject:", threads[0].messages[0].subject)
print("Second sender:", threads[1].messages[0].sender)
print("Second sender:", threads[1].messages[0].subject)