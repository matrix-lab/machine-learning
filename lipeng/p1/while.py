headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = ""

for headline in headlines:
    if len(news_ticker) + len(headline) > 140:
        news_ticker += headline[:(140 - len(news_ticker))]
        if len(news_ticker) == 140:
            break;
    news_ticker += (headline + ' ')

print(news_ticker)

target = []
sources = ['one', 'two', 'three', 'four', 'two', 'five', 'three']


def remove_duplicates(source):
    target = []
    for element in source:
        if element not in target:
            target.append(element)

    return target


print(remove_duplicates(sources))

dictonary = {'name': 'raybon'}

if 'raybon' in dictonary:
    print('123')
