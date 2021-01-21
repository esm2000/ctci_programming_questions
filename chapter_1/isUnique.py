# Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
# cannot use additional data structures?

def isUnique(s):

    dictionary = {}

    # loop through string 
    # store characters in dictionary
    for c in s:
        # if a character is already
        # in the dictionary 
        # return false 
        if c in dictionary:
            return False 

        dictionary[c] = 1

    # if the loop isn't stopped
    # return true 
    return True 

# should result in TTFFFT
print(isUnique('a'),
      isUnique('abc'),
      isUnique('aaaa'),
      isUnique('aabb'),
      isUnique('sungla'),
      isUnique('sunglas'))