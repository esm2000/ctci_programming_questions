import sys
sys.path.insert(1, '../data_structures')
import linkedList

# Remove Dups: Write code to remove duplicates
# from an unsorted linked list.

def removeDups(linkedList):
    # create a dictionary to keep track of elements that 
    # have already appeared 
    record = {}

    # set a pointer for the current node 
    # and another that follows it from 
    # directly behind (prev)
    curr = linkedList.head
    prev = None 

    # iterate through linked list
    while curr:
        # if current element already seen
        if curr.data in record: 
            # set previous node's next address to the node
            # right after the current one (deleting the current)
            prev.next = curr.next
            curr = curr.next
            continue

        # if current element hasn't been seen
        # add it to dictionary
        record[curr.data] = 0
        # and move on 
        prev = curr
        curr = curr.next

llist = linkedList.SLinkedList()
llist.Atbeginning(5)
llist.Atbeginning(5)
llist.Atbeginning(4)
llist.Atbeginning(3)
llist.Atbeginning(3)
llist.Atbeginning(2)
llist.LListprint()

print('')
removeDups(llist)
llist.LListprint()

