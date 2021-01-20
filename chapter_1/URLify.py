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

    for i in range(true_length - 1, -1, -1):
        print(i)
        if s[true_pointer] != ' ':
            output[pointer] = s[true_pointer]
            true_pointer -= 1
            pointer -= 1
        else: 
            output, pointer = replaceSpace(output, pointer)
            true_pointer -= 1
    
    return output

print(URLify(list('Mr John Smith    '), 13))


