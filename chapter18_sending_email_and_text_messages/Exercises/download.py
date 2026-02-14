import ezgmail

threads = ezgmail.search("vacation photos")

# First thread
thread = threads[0]

# First message of the thread
message = thread.messages[0]

# Download a file
message.downloadAttachement("tulips.jpg", downloadFolder="files")
# Download alls files
message.downloadAllAttachments(downloadFolder="files")