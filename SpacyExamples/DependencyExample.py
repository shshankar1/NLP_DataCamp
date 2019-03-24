import spacy
from sklearn.feature_extraction.text import TfidfVectorizer


def main():
    nlp = spacy.load("en_core_web_sm")

    # doc = nlp("Moinian Gets $595 Million Loan to Take Back 3 Columbus Circle")
    # doc = nlp("The Fresh Market to shut 15 stores")
    doc = nlp("SL Green to get $223.3M from selling its stake in 3 Columbus Circle")

    for np in list(doc.noun_chunks):
        np.merge(np.root.tag_, np.root.lemma_, np.root.ent_type_)

    for np in list(doc.noun_chunks):
        if np.root.tag_ == 'NNP':
            print(np.root.text)



if __name__ == "__main__":
    main()
