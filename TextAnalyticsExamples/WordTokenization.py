import nltk


def main():
    sentence = "The brown fox wasn't that quick and he couldn't win the race."
    default_wt = nltk.word_tokenize
    words = default_wt(sentence)
    print(words)


if __name__ == '__main__':
    main()
