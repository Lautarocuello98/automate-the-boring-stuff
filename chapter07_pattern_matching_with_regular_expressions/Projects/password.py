# Lautarocuello98

import re

RULES = {
    "At least 8 characters": lambda s: len(s) >= 8,
    "One uppercase letter": lambda s: bool(re.search(r"[A-Z]", s)),
    "One lowercase letter": lambda s: re.search(r"[a-z]", s),
    "One number":          lambda s: re.search(r"\d", s),
    "One special char":    lambda s: re.search(r"[^\w\s]", s),
}

def check_password(pw: str) -> list[str]:
    pw = pw.strip()
    return [msg for msg, ok in RULES.items() if not ok(pw)]

def main():
    while True:
        pw = input("Password (or 'q' to quit): ").strip()
        if pw.lower() == "q":
            break

        problems = check_password(pw)
        if not problems:
            print("✅ Strong password.")
            break

        print("❌ Weak password:")
        for p in problems:
            print("-", p)

if __name__ == "__main__":
    main()