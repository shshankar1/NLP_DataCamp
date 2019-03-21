import spacy
nlp = spacy.load("en_core_web_lg")

from spacy import displacy

news = open("TheFreshMarket_News.txt",'r')
for line in news:
    doc = nlp(line)
    for x in doc.ents:

        print(x.name, x.label_)
