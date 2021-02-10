import sys
sys.path.insert(1, '../data_structures')
import linkedList

# Delete Middle Node: Implement an algorithm to delete 
# a node in the middle (i.e., any node but
# the first and last node, not necessarily the
# exact middle) of a singly linked list,
# given only access to that node. 

# helper function for testing purposes
# so technically not a part of the 
# problem 
def getMiddleNode(linkedlist):
    
    # two pointers to traverse linked list
    p1 = linkedlist.head
    p2 = linkedlist.head

    while p1.next:
        # pointer 1 travels at two nodes at a time
        p1 = p1.next
        if p1.next is None:
            continue
        p1 = p1.next

        # pointer 2 travels at one node at a time
        p2 = p2.next

    # by the time pointer 1 reaches the end of 
    # list, pointer 2 should point to middle 
    # node
    return p2

# copies next node's info into 
# middle node to "delete" it
def deleteMiddleNode(node):
    node.data = node.next.data
    node.next = node.next.next

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
deleteMiddleNode(getMiddleNode(llist))
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
deleteMiddleNode(getMiddleNode(llist))
llist.LListprint()
        