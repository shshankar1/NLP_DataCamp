from spacy.matcher import Matcher
import spacy


def main():
    nlp = spacy.load('en_core_web_sm')
    doc = nlp("After making the iOS update you won't notice a "
              "radical system-wide redesign: nothing like the aesthetic "
              "upheaval we got with iOS 7. "
              "Most of iOS 11's furniture remains the same as in iOS 10. "
              "But you will discover some tweaks once you delve a little deeper.")

    pattern = [{'TEXT': 'iOS'}, {'IS_DIGIT': True}]

    matcher = Matcher(nlp.vocab)
    matcher.add('IOS_VERSION_PATTERN', None, pattern)
    matches = matcher(doc)
    print('Total matches found:', len(matches))

    for match_id, start, end in matches:
        print('Match found:', doc[start:end].text)


if __name__ == '__main__':
    main()
