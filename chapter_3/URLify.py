def replaceSpace(s):
    
    

    return s

def URLify(s, true_length):

    true_pointer = true_length - 1

    output = ''

    # wanted to use double pointer method for 
    # efficiency but strings are immutable in Python...
    for i in range(true_length - 1, -1, -1):
        if s[true_pointer] != ' ':
            output += s[true_pointer]
            true_pointer -= 1
        else: 
            output += '%'
            output += '0'
            output += '2'
            true_pointer -= 1
    
    return output[::-1]

print(URLify('Mr John Smith    ', 13))

