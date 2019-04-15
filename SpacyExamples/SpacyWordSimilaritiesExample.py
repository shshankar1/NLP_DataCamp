import spacy


def main():
    nlp = spacy.load('en_core_web_lg')

    # in all below examples score were calculated used cosine similarity Word2Vec

    doc1 = nlp('I like fast food')
    doc2 = nlp('I like pizza')

    print(doc1.similarity(doc2))

    doc = nlp('I like pizza and pasta')
    print(doc[2].similarity(doc[4]))

    doc = nlp('I like pizza')
    token = nlp('soap')[0]
    print(doc.similarity(token))

    span = nlp("I like pizza and burger")[2:5]
    doc = nlp('McDonalds sells burger')
    print(span.similarity(doc))

    # Let us take an example of sentimental similarity

    doc1 = nlp('I like cats')
    doc2 = nlp('I hate cats')
    print(doc1.similarity(doc2))

    doc = nlp("This was a great restaurant. Afterwards, we went to a really nice bar.")
    span1 = doc[3:5]
    span2 = doc[-4:-1]
    print(span1.similarity(span2))

    doc1 = nlp('New York')
    doc2 = nlp('NY')
    doc3 = nlp('N York')
    doc4 = nlp('NY.')
    doc5 = nlp('ny')
    print("------------")
    print(doc1.similarity(doc2))
    print(doc1.similarity(doc4))
    print(doc3.similarity(doc4))
    print(doc2.similarity(doc5))


if __name__ == '__main__':
    main()
