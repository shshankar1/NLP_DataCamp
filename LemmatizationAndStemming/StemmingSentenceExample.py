from nltk import word_tokenize
from nltk.stem import PorterStemmer


def stemSentence(sentence):
    words = word_tokenize(sentence)
    stemmer = PorterStemmer()
    word_tokens = []
    for word in words:
        word_tokens.append(stemmer.stem(word))

    return " ".join(word_tokens)


def main():
    sentence = "Pythoners are very intelligent and work very pythonly and now they are pythoning their way to success."
    stemmed_sentence = stemSentence(sentence)
    print(stemmed_sentence)


if __name__ == "__main__":
    main()



