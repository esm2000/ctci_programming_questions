import sys
sys.path.insert(1, '../data_structures')
import linkedList

# Delete Middle Node: Implement an algorithm to delete 
# a node in the middle (i.e., any node but
# the first and last node, not necessarily the
# exact middle) of a singly linked list,
# given only access to that node. 

def deleteMiddleNode(linkedlist):
    
    p1 = linkedlist.head
    p2 = linkedlist.head

    while p1.next:
        p1 = p1.next
        if p1.next is None:
            continue
        p1 = p1.next

        p2_prev = p2
        p2 = p2.next

    p2_prev.next = p2.next

print('Even length')
llist = linkedList.SLinkedList()
llist.Atbeginning('f')
llist.Atbeginning('e')
llist.Atbeginning('d')
llist.Atbeginning('c')
llist.Atbeginning('b')
llist.Atbeginning('a')
llist.LListprint()

print('')
deleteMiddleNode(llist)
llist.LListprint()

print('')
print('Odd length')

llist = linkedList.SLinkedList()
llist.Atbeginning('e')
llist.Atbeginning('d')
llist.Atbeginning('c')
llist.Atbeginning('b')
llist.Atbeginning('a')
llist.LListprint()

print('')
deleteMiddleNode(llist)
llist.LListprint()
        