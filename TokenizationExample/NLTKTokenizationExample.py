from nltk import word_tokenize


def main():
    text = """If you don’t do it, nothing is possible
                    If you do it, at least, you have the hope that there's a chance."""

    tokens = word_tokenize(text)

    print("After NLTK Tokenization, total token counts = %d" % len(tokens))


if __name__ == "__main__":
    main()
