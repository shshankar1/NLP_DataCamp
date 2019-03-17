import spacy


def main():
    nlp = spacy.load('en_core_web_sm')
    doc = nlp("Apple is looking at buying U.K. startup for $1 billion")
    # doc = nlp("I haven't checked complete mail.")
    for token in doc:
        print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
              token.shape_, token.is_alpha, token.is_stop)


if __name__ == "__main__":
    main()
