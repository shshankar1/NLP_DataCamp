import en_core_web_sm


# news sourced from http://www.crenews.com/general_news/general/
# news sourced from https://asreport.americanbanker.com/news/morgan-stanley-ubs-launch-pair-of-cmbs-conduits-totaling-14b


def filter_organizations(entities):
    filtered_items = []
    for entity in entities:
        if entity[1] == 'ORG':
            filtered_items.append(entity)
    return filtered_items


def main():
    news_items = ['Trump to NJ and NY: Build the Hudson River rail tunnel yourselves',
                  'Hudson wins ten-year contract for nine stores at Philadelphia International']
    print(news_items)
    nlp = en_core_web_sm.load()
    entities = []
    for news in news_items:
        doc = nlp(news)
        for X in doc.ents:
            entities.append((X.text, X.label_))

    # org_entities = filter_organizations(entities)
    print("OUTPUT: ")
    print(*entities, sep="\n")


if __name__ == "__main__":
    main()
