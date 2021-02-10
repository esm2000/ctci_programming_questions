import sys
sys.path.insert(1, '../data_structures')
import linkedList

# Remove Dups: Write code to remove duplicates
# from an unsorted linked list.

def removeDups(linkedList):
    record = {}

    curr = linkedList.head
    prev = None 

    while curr:
        if curr.data in record: 
            prev.next = curr.next
            curr = curr.next
            continue

        record[curr.data] = 0
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

