import nltk
from nltk.corpus import gutenberg
from pprint import pprint


def main():
    alice = gutenberg.raw(fileids='carroll-alice.txt')
    sample_text = 'We will discuss briefly about the basic syntax, structure and design philosophies. There is a defined hierarchical syntax for Python code which you should remember when writing code! Python is a really powerful programming language!'
    print(len(alice))

    default_st = nltk.sent_tokenize
    alice_sentences = default_st(text=alice)
    sample_sentences = default_st(text=sample_text)

    print('Total sentences in sample_text:', len(sample_sentences))
    print('Sample text sentences :-')
    pprint(sample_sentences)
    print('\n Total sentences in alice:', len(alice_sentences))
    print('First 5 sentences in alice:-')
    pprint(alice_sentences[0:5])


if __name__ == '__main__':
    main()
