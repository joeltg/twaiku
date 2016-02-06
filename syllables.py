__author__ = 'robert'

import nltk

#load the giant dictionary of words
database = nltk.corpus.cmudict.dict()

#assumptions
#words only contain letters, and they are lowercase

def does_word_exist(word):
    """

    :param word:
    :return: Boolean. True if the word exists in the cmu database. Otherwise, return False.
    """
    try:
        pronunciation = database[word][0]
        return True
    except KeyError, e:
        return False

def count_syllables_word(word):
    """
    Count the number of syllables in a word.
    :param word:
    :return: int, number of syllables in the word. estimate if it doesnt exist in the cmu database
    """
    #check if word exists
    if does_word_exist(word):
        count = 0
        pronunciation = database[word.lower()][0]
        for phenome in pronunciation:
            #if the phenome contains a digit in the last character,
            #then it is a syllable
            if phenome[-1].isdigit():
                count += 1
        return count
    else:
        #TODO
        #estimate the number of syllables
        return 1

def count_syllables_line(line):
    """
    Count the number of syllables in a line of a haiku
    :param line:
    :return: int
    """
    #seperate into words
    words = line.split(" ")
    count = 0
    for word in words:
        syllables = count_syllables_word(word)
        count += syllables
    return count

def count_syllables_haiku(haiku):
    """

    :param haiku: [String]
    :return: [int]
    """
    count = []
    for line in haiku:
        syllables = count_syllables_line(line)
        count.append(syllables)
    return count
