from spacy.matcher import Matcher
import spacy


def main():
    nlp = spacy.load('en_core_web_sm')

    doc = nlp('New iPhone X release date leaked as Apple reveals pre-orders by mistake')

    matcher = Matcher(nlp.vocab)

    pattern = [{'LOWER': 'iphone'}, {'LOWER': 'x'}]
    matcher.add('IPHONE_X_PATTERN', None, pattern)

    matches = matcher(doc)
    print('Matches: ', [doc[start:end].text for match_id, start, end in matches])


if __name__ == '__main__':
    main()
