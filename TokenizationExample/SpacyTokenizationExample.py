import spacy
from spacy.lang.en import English


def main():
    text = """If you don’t do it, nothing is possible
                If you do it, at least, you have the hope that there's a chance."""

    nlp = spacy.load("en_core_web_sm")
    tokenizer = English.Defaults.create_tokenizer(nlp)
    tokens = tokenizer(text)  # implicit __call__ function invoke
    print("After Spacy Tokenization, total tokens in text = %d" %len(tokens))


if __name__ == "__main__":
    main()