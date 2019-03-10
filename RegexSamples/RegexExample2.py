import re


def main():
    my_string = "Let's write RegEx!  " \
                "Won't that be fun?  " \
                "I sure think so.  " \
                "Can you find 4 sentences?  " \
                "Or perhaps, all 19 words?"

    # split the string on sentence terminator
    sentence_ending = "[.?!]"
    print(re.split(sentence_ending, my_string))

    # Find all capitalized words in my_string and print the result
    capitalized_words = "[A-Z]\w+"
    print(re.findall(capitalized_words, my_string))

    # Split my_string on spaces and print the result
    spaces = "\s+"
    print(re.split(spaces, my_string))

    # Find all digits in my_string and print the result
    digits = "\d+"
    print(re.findall(digits, my_string))


if __name__ == "__main__":
    main()