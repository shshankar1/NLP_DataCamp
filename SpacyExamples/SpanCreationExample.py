import spacy


def main():
    nlp = spacy.load('en_core_web_sm')
    text = 'New iPhone X release date leaked as Apple reveals pre-orders by mistake'
    doc = nlp(text)

    for ent in doc.ents:
        print(ent.text, ent.label_)

    iphone_x = doc[1:3]

    print('Missing Entity: %s' % iphone_x.text)


if __name__ == '__main__':
    main()
