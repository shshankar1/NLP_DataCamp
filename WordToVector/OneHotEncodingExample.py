import numpy as np


def create_vocabulary(text):
    word_dict = {}
    vocabulary_size = 0
    for word in text.split(" "):
        # If we are seeing this word for the first time, create an id for it and added it to our word dictionary
        if word not in word_dict:
            word_dict[word] = vocabulary_size
            vocabulary_size += 1
    return word_dict


def one_hot(word, word_dict):
    vector = np.zeros(len(word_dict))
    vector[word_dict[word]] = 1
    return vector


def main():
    text = """If you don’t do it, nothing is possible
                If you do it, at least, you have the hope that there's a chance."""
    vocab = create_vocabulary(text)
    word_vector = one_hot('nothing', vocab)
    print(word_vector)


if __name__ == "__main__":
    main()
