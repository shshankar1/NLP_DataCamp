import spacy
from spacy.matcher import Matcher


def main():
    nlp = spacy.load('en_core_web_sm')
    doc = nlp("i downloaded Fortnite on my laptop "
              "and can't open the game at all. Help? "
              "so when I was downloading Minecraft, "
              "I got the Windows version where it is the '.zip' folder "
              "and I used the default program to unpack it... "
              "do I also need to download Winzip?")

    pattern = [{'LEMMA': 'download'}, {'POS': 'PROPN'}]
    matcher = Matcher(nlp.vocab)
    matcher.add('DOWNLOAD_THINGS_PATTERN', None, pattern)
    matches = matcher(doc)
    print('Total matches found:', len(matches))

    for match_id, start, end in matches:
        print('Match found:', doc[start:end].text)


if __name__ == '__main__':
    main()
