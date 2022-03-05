import codecs
import os

import ru_core_news_md

nlp = ru_core_news_md.load()

pages = os.listdir('pages')
print(pages)

for page in pages:
    text = codecs.open('pages/' + page, encoding='utf-8', mode='r').read()
    document = nlp(text)
    with open('lemm/' + page, 'w', encoding='utf8') as out:
        for token in document:
            # Get the lemma for each token
            out.write(token.lemma_.lower())
            # Insert white space between each token
            out.write(' ')
