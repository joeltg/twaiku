import nltk
nltk.data.path.append("./nltk_data")

database = nltk.corpus.wordnet.synset('dog.n.01')

print database.name()