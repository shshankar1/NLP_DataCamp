from spacy.lang.en import English


def main():
    nlp = English()
    doc = nlp("""In 1990, more than 60% of people in East Asia were in extreme poverty. 
              Now less than 4% are.""")

    for token in doc:
        if token.like_num:
            next_token = doc[token.i + 1]
            if next_token.text == '%':
                print("Percentage Found: %s" % token.text)


if __name__ == "__main__":
    main()
