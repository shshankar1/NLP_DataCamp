import spacy

from spacy.lang.en import English
from spacy.lang.de import German


def main():
    nlp = spacy.load('en_core_web_sm')

    cat_hash = nlp.vocab.strings['cat']
    print(cat_hash)

    cat_string = nlp.vocab.strings[cat_hash]
    print(cat_string)

    nlp = English()
    nlp_de = German()

    bowie_id = nlp.vocab.strings['Bowie']
    print(bowie_id)

    # bowie_string = nlp_de.vocab.strings[bowie_id]
    # print(bowie_string)


if __name__ == '__main__':
    main()
