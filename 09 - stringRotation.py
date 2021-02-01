# Assume you have a method isSubstring which checks if oneword
# is a substring of another. Given two strings, sl and s2,
# write code to check if s2 is a rotation of sl using only one
# call to isSubstring (e.g., "waterbottle" is a rotation
# of"erbottlewat").

def isSubstring(s1, s2):
    return s2 in s1

def stringRotation(s1, s2):
    # a rotated string concatenated with itself will
    # contain the original string somewhere in it
    s3 = s2 + s2

    return isSubstring(s3, s1)    

print(stringRotation('waterbottle', 'erbottlewat'))