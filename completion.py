import nltk
from syllables import count_syllables_word
from nltk.corpus import brown
from nltk.probability import LidstoneProbDist

words = nltk.corpus.brown.words()
words += nltk.corpus.gutenberg.words()
words += nltk.corpus.reuters.words()

est = lambda fdist, buns: LidstoneProbDist(fdist, 0.2)
model = nltk.NgramModel(3, brown.words(), estimator=est)

def get_next_words(path):
    context = [c[0] for c in path]
    words = set([])
    for i in range(50):
        word = model.choose_random_word(context)
        if word.isalpha():
            words.add(word)
    return list(words)
