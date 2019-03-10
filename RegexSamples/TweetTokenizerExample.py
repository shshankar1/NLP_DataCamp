from nltk.tokenize import regexp_tokenize, TweetTokenizer


def main():
    tweets = ['This is the best #nlp exercise ive found online! #python',
             '#NLP is super fun! <3 #learning',
             'Thanks @datacamp :) #nlp #python']
    pattern1 = '#\w+'
    tokens = regexp_tokenize(tweets[0], pattern1)
    print(tokens)

    pattern2 = '[#|@]\w+'
    tokens = regexp_tokenize(tweets[-1], pattern2)
    print(tokens)

    tknzr = TweetTokenizer()
    all_tokens = [tknzr.tokenize(t) for t in tweets]

    print(all_tokens)

if __name__ == '__main__':
    main()