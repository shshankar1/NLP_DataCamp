import spacy


def main():
    nlp = spacy.load("en_core_web_lg")
    tokens = nlp("god dog cat banana")

    for token1 in tokens:
        for token2 in tokens:
            print(token1, token2, token1.similarity(token2))


if __name__ == "__main__":
    main()
