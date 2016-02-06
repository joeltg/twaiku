from oxford import get_candidates, get_candidates_in_range

def complete_range(string, max_syllables):
    # here candidates are list of tuples of (word, syllable_count)
    def candidate_to_string(candidate):
        return string + ' ' + ' '.join([c[0] for c in candidate])

    completion = []

    # queue is a list of (string, [words...]).
    queue = [[c] for c in get_candidates_in_range(string, max_syllables)]

    while len(queue) > 0:
        candidate = queue.pop()
        s = sum([c[1] for c in candidate])
        if s == max_syllables:
            return candidate
        next_candidates = get_candidates_in_range(candidate_to_string(candidate), max_syllables - s)
        queue += [candidate + [c] for c in next_candidates]

    print 'could not complete'

print complete_range('my', 13)
