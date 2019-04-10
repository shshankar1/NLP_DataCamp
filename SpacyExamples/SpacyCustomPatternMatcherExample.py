import spacy
from spacy.matcher import Matcher


def main():
    nlp = spacy.load('en_core_web_sm')
    doc = nlp("Features of the app include a beautiful design, "
              "smart search, automatic labels and optional voice responses.")

    matcher = Matcher(nlp.vocab)
    pattern = [{'POS': 'ADJ'}, {'POS': 'NOUN'}, {'POS': 'NOUN', 'OP': '?'}]
    matcher.add('ADJ_NOUN_PATTERN', None, pattern)
    matches = matcher(doc)

    print('Total matches found: ', len(matches))

    for match_id, start, end in matches:
        print('Match found: ', doc[start:end].text)


if __name__ == '__main__':
    main()
