import re

def regex_strip(text, chars=None):
    if chars is None:
        return re.sub(r'^\s+|\s+$', '', text)
    else:
        chars = re.escape(chars)
        return re.sub(rf'^[{chars}]+|[{chars}]+$', '', text)
    
# Example usage:
def main():
    text = input("Enter text to strip: ")
    print(regex_strip(text))



if __name__ == "__main__":
    main()