# URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string
# has sufficient space at the end to hold the additional characters, and that you are given the "true"
# length of the string. (Note: if implementing in Java, please use a character array so that you can
# perform this operation in place.) 

# this helper function replaces a space (or any
# character) at a given index with 20%, provided the
# string has enough space 
def replaceSpace(s, index):
    
    s[index] = '%'
    index -= 1
    s[index] = '0'
    index -= 1
    s[index] = '2'
    index -= 1

    return s, index

def URLify(s, true_length):

    true_pointer = true_length - 1
    pointer = len(s) - 1

    output = [''] * len(s)

    # count backwards from the "true length" of the string
    # (the string before the trailing whitespace) 
    for i in range(true_length - 1, -1, -1):
        # shift the position of non-space characters to 
        # accommodate the extra indexes taken up by 
        # switching the ' 's to '20%'
        if s[true_pointer] != ' ':
            output[pointer] = s[true_pointer]
            true_pointer -= 1
            pointer -= 1
        else: 
            # replace any spaces found with 20%
            output, pointer = replaceSpace(output, pointer)
            true_pointer -= 1
    
    return output

print(URLify(list('Mr John Smith    '), 13))


