import Levenshtein


def main():
    text1 = "Software Engineer"
    text2 = "Software Developer"
    print(Levenshtein.ratio(text1, text2))


if __name__ == '__main__':
    main()
