import nltk
nltk.data.path.append("./nltk_data")

database = nltk.corpus.wordnet

<<<<<<< HEAD
print database.name()
=======
#assume word is valid and all lowerecase
def get_synonyms(word):
    words = []
    synonyms = database.synsets(word)
    for elt in synonyms:
        names = elt.lemma_names()
        for name in names:
            name = str(name)
            #replace hyphens with a space
            name = name.replace("-", " ")
            if name not in words:
                words.append(name)
    #sometimes it will return the same word as a synonym, remove from list to be safe
    words.remove(word)
    return words
>>>>>>> bee40f26653507d77eb16ae058ee9b9e5f152422
