import spacy
from spacy import displacy


def main():
    nlp = spacy.load("en_core_web_sm")
    tagger = nlp.tagger

    doc = nlp("The sailor dogs the hatch.")
    processed = tagger(doc)
    for t in processed:
        print(t.text, t.pos_, t.tag_, t.dep_, t.head)

    displacy.serve(doc, style='dep')


if __name__ == "__main__":
    main()
