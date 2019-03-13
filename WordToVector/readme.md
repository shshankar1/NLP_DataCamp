A good reading resource on Word-to-Vector https://towardsdatascience.com/word-to-vectors-natural-language-processing-b253dd0b0817

Root idea is every language has millions of words and it is impossible for a machine to store every word as form of vocabulary.

So there are set of basic NLP algorithm which try to solve this problem.

How efficient is the algorithm depends on effective representation of word in vector format and saving memory space.

For example OneHotEncoding is one way of doing word vectorization but it is kind of worst technique because every word will be represented as vector having n elements which is equal to total vocabulary size. 