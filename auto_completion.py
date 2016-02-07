import nltk

nltk.data.path.append("./nltk_data")

import trie

database = trie.Trie()
words = nltk.corpus.webtext.words()
words += nltk.corpus.nps_chat.words()
#words += nltk.corpus.brown.words()
#words += nltk.corpus.gutenberg.words()
#words += nltk.corpus.reuters.words()

for word in words:
    database.insert(word)

def auto_complete(word):
    return database.autocomplete(word)

print auto_complete('hel')