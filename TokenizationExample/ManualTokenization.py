import string


def extract_tokens(text):
    temp = text.split(" ")
    text_words = []

    for word in temp:
        if len(word) > 0:
            # removing punctuations char from beginning of word
            while word[0] in string.punctuation:
                word = word[1:]

            while word[-1] in string.punctuation:
                word = word[:-1]

            text_words.append(word)

    return text_words


def main():
    text = """If you don’t do it, nothing is possible
            If you do it, at least, you have the hope that there's a chance."""

    tokens = extract_tokens(text)
    print("After Manual Tokenization, Total tokens in text: %d" % len(tokens))


if __name__ == "__main__":
    main()
