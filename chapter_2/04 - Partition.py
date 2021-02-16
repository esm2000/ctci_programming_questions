import sys
sys.path.insert(1, '../data_structures')
import linkedList

# Write code to partition a linked list around a value x,
# such that all nodes less than x come before all nodes
# greater than or equal to x. If x is contained within
# the list, the values of x only need to be after the
# elements less than x (see below). The partition element
# x can appear anywhere in the "right partition"; it
# does not need to appear between the left and right partitions.

def partition(llist_head, x):

    # references for nodes with values
    # less than and greater than x
    less_head, less_tail = None, None 
    greater_head, greater_tail = None, None 

    # traverse linked list
    curr = llist_head
    next_node = None 

    while curr:
        next_node = curr.next 

        curr_copy = linkedList.Node(curr.data)
        # if curr node's value is less than x 
        # insert it into less_nodes 
        # and delete from input list
        if curr.data < x:
            if less_head is None: 
                less_head = curr_copy
                less_tail = curr_copy
            else: 
                curr_copy.next = less_head
                less_head = curr_copy
        # if curr node's value is equal to or 
        # greater than x insert it into
        # greater_nodes and delete from
        # input list 
        else: 
            if greater_head is None:
                greater_head = curr_copy 
                greater_tail = curr_copy
            else:
                curr_copy.next = greater_head
                greater_head = curr_copy

        curr = next_node

    # connect less than nodes to greater than nodes 
    less_tail.next = greater_head

    return less_head 
    
llist = linkedList.SLinkedList()
llist.Atbeginning(1)
llist.Atbeginning(2)
llist.Atbeginning(10)
llist.Atbeginning(5)
llist.Atbeginning(8)
llist.Atbeginning(5)
llist.Atbeginning(3)
llist.LListprint()

ans = partition(llist.head, 5)
print('')
ans_str = ''

curr = ans 
while curr: 
    ans_str += str(curr.data)
    ans_str += ' '
    curr = curr.next

print(ans_str)
   



    




