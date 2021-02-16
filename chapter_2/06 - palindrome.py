import sys
sys.path.insert(1, '../data_structures')
import linkedList
import copy 

# Implement a function to check if a linked list is a palindrome
def palindrome(llist):

    # reverse the linked list 
    # while preserving original 
    original_llist = copy.deepcopy(llist)

    prev_node = None
    curr_node = llist
    next_node = None

    while curr_node:
        next_node = curr_node.next
        curr_node.next = prev_node
        prev_node = curr_node
        curr_node = next_node 

    reverse_llist = prev_node
    # iterate through both at the same time
    # return False if there are node
    # values that don't match
    curr = original_llist
    reverse_curr = reverse_llist

    while curr:
        if curr.data != reverse_curr.data:
            return False
        
        curr = curr.next
        reverse_curr = reverse_curr.next

    return True 

word1 = linkedList.SLinkedList()
word1.Atbeginning('m')
word1.Atbeginning('a')
word1.Atbeginning('d')
word1.Atbeginning('a')
word1.Atbeginning('m')
word1.LListprint()

print('')
print(palindrome(word1.head))

word2 = linkedList.SLinkedList()
word2.Atbeginning('m')
word2.Atbeginning('a')
word2.Atbeginning('d')
word2.Atbeginning('a')
word2.LListprint()

print('')
print(palindrome(word2.head))