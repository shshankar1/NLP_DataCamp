from nltk.corpus import wordnet as wn


def main():
    word = 'hike'
    word_synset = wn.synsets(word)
    print(word_synset)

    for syn in word_synset:
        print('Synset Name:', syn.name())
        print('POS Tag:', syn.pos())
        print('Definition:', syn.definition())
        print('Examples:', syn.examples())
        print("------------------")


if __name__ == "__main__":
    main()
