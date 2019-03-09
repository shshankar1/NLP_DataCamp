from nltk.stem import LancasterStemmer
from nltk.stem import PorterStemmer
from nltk.stem import SnowballStemmer

def main():
    lancaster = LancasterStemmer()
    porter = PorterStemmer()
    snowball = SnowballStemmer("english")

    word_list = ["friend", "friendship", "friends",
                 "friendships", "stabil", "destabilize",
                 "misunderstanding", "universe", "universal",
                 "university", "union",
                 "railroad", "moonlight", "football", "going",
                 "education"]
    print("{0:20}{1:20}{2:20}{3:20}".format("Word", "Porter Stemmer", "lancaster Stemmer", "Snowball Stemmer"))
    for word in word_list:
        print("{0:20}{1:20}{2:20}{3:20}".format(word, porter.stem(word), lancaster.stem(word), snowball.stem(word)))


if __name__ == "__main__":
    main()