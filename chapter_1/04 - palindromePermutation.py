# Palindrome Permutation: Given a string, write a function to check if it is a permutation of
# a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A
# permutation is a rearrangement of letters. The palindrome does not need to be limited to just
# dictionary words.

def palindromePermutation(s):

    # make string lowercase and strip it 
    # of all it's spaces 
    s = s.lower().replace(' ', '')

    d = {}

    # count the letter occurences in a 
    # dictionary (letter: count)
    for l in s: 
        if l in d: 
            d[l] += 1
        else:
            d[l] = 1

    # if the string is odd in length 
    # allow one occurence of an odd count
    if len(s) % 2 == 1:
        flag = False
        for l in d:
            if d[l] % 2 == 1:
                if flag: 
                    return False 
                flag = True 
    # if the string is even in length 
    # allow no occurences of an even count 
    else: 
        for l in d: 
            print('%s: %d' % (l, d[l]))
            if d[l] % 2 == 1:
                return False 

    return True 

print(palindromePermutation('Tact Coa'))
