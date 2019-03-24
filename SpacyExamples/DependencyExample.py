import spacy
import pandas as pd


def main():
    nlp = spacy.load("en_core_web_sm")

    # doc = nlp("Moinian Gets $595 Million Loan to Take Back 3 Columbus Circle")
    # doc = nlp("The Fresh Market to shut 15 stores")
    doc = nlp("SL Green to get $223.3M from selling its stake in 3 Columbus Circle")

    for np in list(doc.noun_chunks):
        np.merge(np.root.tag_, np.root.lemma_, np.root.ent_type_)

    filtered_docs = []
    for np in list(doc.noun_chunks):
        if np.root.tag_ == 'NNP':
            # creating doc of output
            filtered_docs.append(nlp(np.root.text))
            # print(np.root.text)

    # create dataframe from Trepp Db properties name
    df = pd.DataFrame(columns=["ExtractedEntity", "DealName", "PropertyName", "SpacyDoc"])

    db_props_dict = {"ALM4": "Angelo Gorden",
                     "XYZ": "2 Columbus Circle",
                     "ABC": "3 Columbus Circle"}

    for i, key in enumerate(db_props_dict):
        df.loc[i] = None, key, db_props_dict[key], nlp(db_props_dict[key])

    result = pd.DataFrame(columns=["ExtractedEntity", "MatchedDeals"])

    temp_df = df.copy(deep=True)
    for docx in filtered_docs:
        temp_df['ExtractedEntity'] = docx.text
        temp_df['MatchScore'] = temp_df['SpacyDoc'].apply(lambda doc: doc.similarity(docx))
        temp_df.drop('SpacyDoc', axis=1, inplace=True)

    temp_df = temp_df[temp_df['MatchScore'] > 0.9]
    print(temp_df.to_json(orient='records'))


if __name__ == "__main__":
    main()
