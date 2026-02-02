import re

def main():
    while True:
        password = input("give me a password: ")
        result = strong_password(password)
        print(result)
        if result == 'perfect':
            break




def strong_password(password):
        if len(password) < 8:
            return 'need have 8 caracters or more'
        if not re.search(r'[A-Z]', password):
            return 'need any uppercase'
        if not re.search(r'[a-z]', password):
            return 'need any lowercase'
        if not re.search(r'\d', password):
            return 'need any number'
        return 'perfect'
        


if __name__ == "__main__":
    main()