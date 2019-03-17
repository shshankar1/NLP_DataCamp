import spacy
import en_core_web_sm


def first_way_to_load_spacy():
    nlp = spacy.load('en_core_web_sm')
    return nlp


def second_way_to_load_spacy():
    return en_core_web_sm.load()


def main():
    # nlp = first_way_to_load_spacy()
    nlp = second_way_to_load_spacy()
    doc = nlp.__call__("I like NLP/ML")
    for word in doc:
        print(word.text, word.pos_, word.dep_)


if __name__ == "__main__":
    main()
