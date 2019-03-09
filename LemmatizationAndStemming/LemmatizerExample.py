from nltk.stem import WordNetLemmatizer
from nltk import word_tokenize
from nltk.corpus import stopwords

lemmatizer = WordNetLemmatizer()


def lemmatize_sentence(sentence, punctuations):
    words = word_tokenize(sentence)
    tokens = []
    stop_words = set(list(stopwords.words("english")) + list(punctuations))
    # for word in [word for word in words if word not in punctuations]:
    #    tokens.append(lemmatizer.lemmatize(word))
    for word in words:
        if word not in stop_words:
            tokens.append(lemmatizer.lemmatize(word))
    return " ".join(tokens)


def main():
    sentence = "He was running and eating at same time. He has bad habit of swimming after playing long hours in the Sun."
    punctuations = "?:!.,;"
    lemmas = lemmatize_sentence(sentence, punctuations)
    print("--------------------")
    print("Actual Sentence: ")
    print(sentence)
    print("--------------------")
    print("Lemmatized Sentence:")
    print(lemmas)
    print("--------------------")


if __name__ == "__main__":
    main()

