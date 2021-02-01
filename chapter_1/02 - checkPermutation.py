# Check Permutation: Given two strings, write a method to decide if one is a permutation of the
# other.


def checkPermutation(s1, s2):

    # if the two strings are not equal in length
    # they can't be permutations
    if len(s1) != len(s2):
        return False

    d = {}

    # have a dictionary that keeps track of
    # the number of times letters appear in
    # the first word
    for c in s1:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1

    # remove letters that are accounted for in
    # the second word
    for c in s2:
        if c not in d:
            return False

        d[c] -= 1

    # if the final count of any letters is not 0
    # the words are not permutations
    for c in d:
        if d[c] != 0:
            return False

    return True


# should result in TTFF
print(checkPermutation('abc', 'abc'),
      checkPermutation('abc', 'cba'),
      checkPermutation('a', 'ab'),
      checkPermutation('abc', 'abe'))
