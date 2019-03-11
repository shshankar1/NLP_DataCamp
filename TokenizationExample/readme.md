<pre>
Tokenization is one of step which comes under data preprocessing pipeline.

Major usecase of tokenization is reduce the memory footprint for large text.

e.g.
Let us assume sample text is
"""If you don’t do it, nothing is possible
   If you do it, at least, you have the hope that there's a chance."""

I can prepare a vocabulary with all words in text with some unique number 
and then put that number in text as placeholder.

{
    If -> 0
    you -> 1
    don't -> 2
    do -> 3
    it -> 4
    nothing -> 5
    is -> 6
    possible -> 7
    at -> 8
    least -> 9
    have -> 10
    the -> 11
    hope -> 12
    that -> 13
    there's -> 14
    a -> 15
    chance -> 16
}

Now putting numbers in text as placeholder
 [0 1 2 3 4, 5 6 7. 0 1 3 4, 8 9, 1 10 11 12 13 14 15 16]
 
So there are 22 words in text, and by doing tokenization we saved space 
by just having 16 words and place holders.

Basically NLP models use tokenization to reduce memory footprint without 
loosing any information

Now we are going to implement tokenization in 3 ways:
1. Manual Tokenization
2. NLTK library of tokenization
3. Spacy Tokenization

</pre>
