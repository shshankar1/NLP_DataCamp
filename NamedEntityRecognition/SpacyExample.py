import en_core_web_sm


# news sourced from http://www.crenews.com/general_news/general/
# news sourced from https://asreport.americanbanker.com/news/morgan-stanley-ubs-launch-pair-of-cmbs-conduits-totaling-14b

def read_news(file):
    news_items = []
    buffer = None
    for line in open(file):
        if line != "------\n":
            line = line.replace("\n", " ")  # replace new-line by space
            buffer = line if buffer is None else buffer + line
        else:
            news_items.append(buffer)
            buffer = None
    return news_items


def filter_organizations(entities):
    filtered_items = []
    for entity in entities:
        if entity[1] == 'ORG':
            filtered_items.append(entity)
    return filtered_items


def main():
    news_items = read_news("news.txt")
    print(news_items)
    nlp = en_core_web_sm.load()
    entities = []
    for news in news_items:
        doc = nlp(news)
        for X in doc.ents:
            entities.append((X.text, X.label_))

    org_entities = filter_organizations(entities)
    print("OUTPUT: ")
    print(*org_entities, sep="\n")


if __name__ == "__main__":
    main()
