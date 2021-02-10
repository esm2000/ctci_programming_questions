import sys
sys.path.insert(1, '../data_structures')
import linkedList

# Return Kth to Last: Implement an algorithm to
# find the kth to last element of a singly linked list. 

def returnKthToLast(linked_list, k):

    curr = linked_list.head
    length = 1

    while curr:
        curr = curr.next
        if curr:
            length += 1

    j = length - k + 1

    for i in range(j):
        if i == 0:
            curr = linked_list.head
        else:
            curr = curr.next
    
    return curr.data

llist = linkedList.SLinkedList()
llist.Atbeginning(5)
llist.Atbeginning(4)
llist.Atbeginning(3)
llist.Atbeginning(2)
llist.Atbeginning(1)
llist.LListprint()

k = 4
ans = returnKthToLast(llist, k)
print('')
print('%dth to Last Element in Linked List is %d' % (k, ans))
