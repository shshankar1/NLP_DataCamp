import spacy
from spacy.tokens import Doc


def main():
    nlp = spacy.load("en_core_web_lg")
    doc = Doc(nlp.vocab,
              words=['This', 'is', 'a', 'sentence'],
              spaces=[True, True, True, True])
    for word in doc:
        print(word)


if __name__ == "__main__":
    main()
