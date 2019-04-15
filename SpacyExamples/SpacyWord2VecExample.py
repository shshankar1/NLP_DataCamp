import spacy


def main():
    nlp = spacy.load('en_core_web_lg')

    doc = nlp('2 bananas in pyjamas')
    token = doc[1]
    print(token.vector)


if __name__ == '__main__':
    main()
