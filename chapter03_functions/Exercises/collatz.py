def main():
    print("give me a number: ")
    user_input = input()
    n = int(user_input)
    collatz(n)

def collatz(n):
    try:
        if n <= 0:
            print("Please enter a positive integer.")
            return
        while n != 1:
            if n % 2 == 0:
                n = n // 2
            else:
                n = 3 * n + 1
            print(n)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()