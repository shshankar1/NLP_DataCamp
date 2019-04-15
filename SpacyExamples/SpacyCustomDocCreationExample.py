from spacy.tokens import Doc
import spacy


def main():
    nlp = spacy.load('en_core_web_sm')
    words = ['Spacy', 'is', 'cool', '!']
    spaces = [True, True, False, False]

    doc = Doc(nlp.vocab, words=words, spaces=spaces)
    print(doc.text)

    words = ['Go', ',', 'Get', 'Started', '!']
    spaces = [False, True, True, False, False]

    doc = Doc(nlp.vocab, words=words, spaces=spaces)
    print(doc.text)


if __name__ == '__main__':
    main()
