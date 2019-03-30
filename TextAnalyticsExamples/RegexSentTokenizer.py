import nltk
from pprint import pprint


def main():
    SENTENCE_TOKENS_PATTERN = r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<![A-Z]\.)(?<=\.|\?|\!)\s'
    regex_st = nltk.tokenize.RegexpTokenizer(pattern=SENTENCE_TOKENS_PATTERN, gaps=True)
    sample_text = 'We will discuss briefly about the basic syntax, structure and design philosophies. There is a defined hierarchical syntax for Python code which you should remember when writing code! Python is a really powerful programming language!'
    sample_sentences = regex_st.tokenize(sample_text)
    pprint(sample_sentences)


if __name__ == '__main__':
    main()
