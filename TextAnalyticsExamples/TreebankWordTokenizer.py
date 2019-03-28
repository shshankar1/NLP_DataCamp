import nltk


def main():
    sentence = "The brown fox wasn't that quick and he couldn't win the race."
    tokenizer = nltk.TreebankWordTokenizer()
    words = tokenizer.tokenize(sentence)
    print(words)


if __name__ == "__main__":
    main()
