import nltk
from pprint import pprint


def main():
    sample_text = 'We will discuss briefly about the basic syntax, structure and design philosophies. There is a defined hierarchical syntax for Python code which you should remember when writing code! Python is a really powerful programming language!'
    punkt_st = nltk.tokenize.PunktSentenceTokenizer()
    sample_sentences = punkt_st.tokenize(sample_text)
    pprint(sample_sentences)


if __name__ == '__main__':
    main()
