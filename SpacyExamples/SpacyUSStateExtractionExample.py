import spacy
from spacy.pipeline import EntityRuler

list_of_states = ['fl', 'florida', 'FL']


def main():
    nlp = spacy.load('en_core_web_lg')
    # us_state_entity_matcher = USStatesEntityMatcher(nlp, list_of_states, 'STATE')
    us_state_entity_matcher = EntityRuler(nlp)
    us_city_entity_matcher = EntityRuler(nlp)
    state_patterns = [
        {"label": "STATE", "pattern": [{'lower': "fl"}]}
    ]
    city_patterns = [
        {"label": "CITY", "pattern": [{'lower': "fl"}]}
    ]
    us_state_entity_matcher.add_patterns(state_patterns)
    us_state_entity_matcher.add_patterns(city_patterns)
    nlp.add_pipe(us_state_entity_matcher, before='ner')
    # nlp.add_pipe(us_city_entity_matcher, before='ner')
    print(nlp.pipe_names)
    text1 = 'Reality market is picking up in FL'
    # text2 = 'Florida is witnessing speedy growth in real estate market'

    doc1 = nlp(text1)

    print([(ent.text, ent.label_) for ent in doc1.ents])


if __name__ == '__main__':
    # sys.setrecursionlimit(100000)
    main()
