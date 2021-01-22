# Implement a method to perform basic string compression using the
# counts of repeated characters. For example, the string aabcccccaaa
# would become a2blc5a3. If the "compressed" string would not become
# smaller than the original string, your method should return
# the original string. You can assume the string has only uppercase
# and lowercase letters (a - z)

def stringCompression(s):
    output = ''
    curr_count = 0 

    # loop through the string 
    for i in range(len(s)):

        # on the first character set the curr_count to 1
        if i == 0:
            curr_count += 1
        else:
            # if the current character is the same as the last
            # update count and move on 
            if s[i - 1] == s[i]:
                curr_count += 1
            # if the current character is different from the 
            # the last update the output string and reset count
            else: 
                output += s[i - 1] + str(curr_count)
                curr_count = 1
            
            # on the last character update output string 
            if i == len(s) - 1:
                output += s[i] + str(curr_count)

    # if the output string is shroter than the input string return
    # input string 
    if len(s) < len(output):
        return s 
    # otherwise return output string 
    else: 
        return output 

print(stringCompression('aabcccccaaa'))    
print(stringCompression('aabcccccaaad'))    