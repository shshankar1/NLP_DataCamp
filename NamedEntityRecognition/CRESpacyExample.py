import en_core_web_lg


def main():
    news = 'Rancho Mirage, a 310-unit multifamily property located in the Las Colinas master-planned community, recently underwent $2 million in property improvements to overhaul units and amenities for 3 Columbus Circle.'
    nlp = en_core_web_lg.load()
    doc = nlp(news)
    for np in list(doc.noun_chunks):
        np.merge(np.root.tag_, np.root.lemma_, np.root.ent_type_)

    for ent in doc.ents:
        print(ent.text, ent.label, ent.lemma_, ent.root.ent_type)


if __name__ == '__main__':
    main()
