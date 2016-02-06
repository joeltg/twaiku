from oxford import get_candidates, get_candidates_in_range
from syllables import count_syllables_haiku

# here candidates are list of tuples of (word, syllable_count)
def candidate_to_string(candidate):
    return ' '.join([c[0] for c in candidate])

def complete_range(string, max_syllables):

    completion = []

    # queue is a list of (string, [words...]).
    queue = [[c] for c in get_candidates_in_range(string, max_syllables)]

    while len(queue) > 0:
        candidate = queue.pop()
        s = sum([c[1] for c in candidate])
        if s == max_syllables:
            return candidate
        next_candidates = get_candidates_in_range(string + ' ' + candidate_to_string(candidate), max_syllables - s)
        queue += [candidate + [c] for c in next_candidates]

    print 'could not complete'

def complete_haiku(haiku):
    # haiku is a list of strings
    haiku_count = count_syllables_haiku(haiku)

    # first line
    max_syllables = 5 - haiku_count[0]
    if max_syllables > 0:
        haiku[0] = candidate_to_string(complete_range(haiku[0], max_syllables))
    elif max_syllables < 0:
        print('this is bad')

    # second line
    max_syllables = 7 - haiku_count[1]
    if max_syllables > 0:
        haiku[1] = candidate_to_string(complete_range(haiku[0] + ' ' + haiku[1], max_syllables))
    elif max_syllables < 0:
        print('this is bad')

    # third line
    max_syllables = 5 - haiku_count[2]
    if max_syllables > 0:
        haiku[2] = candidate_to_string(complete_range(haiku[0] + ' ' + haiku[1] + ' ' + haiku[2], max_syllables))
    elif max_syllables < 0:
        print('this is bad')

    return haiku

print complete_haiku(['yesterday I ate', 'a', ''])
