# One Away: There are three types of edits that can be
# performed on strings: insert a character, remove a
# character, or replace a character. Given two strings,
# write a function to check if they are one edit (or
# zero edits) away.


def oneAway(s1, s2):

    # if the two strings are equal return True
    if s1 == s2:
        return True

    # if the two strings are not equal and their length
    # differs more than 1 return False
    if abs(len(s1) - len(s2)) > 1:
        return False

    diff = 0
    d = {}

    # create a dictionary that keeps track of character
    # counts in first string
    for c in s1:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    # loops through second string and decrements
    # count by 1 if character is present in first string
    # increments count by 1 if character not present in
    # first string
    for c in s2:
        if c in d:
            d[c] -= 1
        else:
            d[c] = 1

    # takes sum of counts as the num character
    # difference between the two strings
    for letter in d:
        diff += d[letter]
    # [insert or remove a character] diff count of 1
    if abs(len(s1) - len(s2)) == 1:
        return diff == 1
    # [replace a character] diff count of 2
    else:
        return diff == 2


print(oneAway('pale', 'ple'))
print(oneAway('pales', 'pales'))
print(oneAway('pale', 'bale'))
print(oneAway('pale', 'bae'))
