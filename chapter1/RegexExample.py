
import re

def main():
    PATTERN = "\w+"
    my_string = "Let's write RegEx"
    print(re.findall(PATTERN, my_string))

if __name__ == "__main__":
    main()