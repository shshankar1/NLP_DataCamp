from spacy.lang.en import English
from spacy.lang.de import German
from spacy.lang.es import Spanish


def main():
    nlp = English()
    doc = nlp("This is a sentence.")
    print(doc.text)

    nlp = German()
    doc = nlp('Liebe Grüße!')
    print(doc.text)

    nlp = Spanish()
    doc = nlp('¿Cómo estás?')
    print(doc.text)


if __name__ == '__main__':
    main()
