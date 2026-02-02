import random

messages = [
    'it is certain',
    'it is decidedly so',
    'reply hazy try again',
    'ask again later',
    'concetrate and ask again',
    'my reply is no',
    'outlook not so good',
    'very doubtful'
]

print(messages[random.randint(0, len(messages) - 1)])