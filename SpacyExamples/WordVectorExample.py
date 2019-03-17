import spacy


def main():
    nlp = spacy.load("en_core_web_lg")
    tokens = nlp("dog cat banana afskfsd")

    for token in tokens:
        print(token.text, token.has_vector, token.vector_norm, token.is_oov)


if __name__ == "__main__":
    main()
