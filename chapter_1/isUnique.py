def isUnique(s):

    dictionary = {}

    for c in s:
        if c in dictionary:
            return False 

        dictionary[c] = 1

    return True 

# should result in TTFFFT
print(isUnique('a'),
      isUnique('abc'),
      isUnique('aaaa'),
      isUnique('aabb'),
      isUnique('sungla'),
      isUnique('sunglas'))