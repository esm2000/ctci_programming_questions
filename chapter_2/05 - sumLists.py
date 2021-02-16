import sys
sys.path.insert(1, '../data_structures')
import linkedList

# You have two numbers represented by a linked
# list, where each node contains a single
# digit. The digits are stored in reverse 
# order, such that the 1 's digit is at 
# the head of the list. Write a
# function that adds the two numbers
# and returns the sum as a linked list. 

def sumLists(num1, num2):
    
    multiplier = 1

    num1_curr = num1
    num2_curr = num2
    ans = 0
    
    # iterate through both lists,
    # stopping when both pointers 
    # are null
    while num1_curr is not None or num2_curr is not None:
        
        # add product of multiplier
        # and each num to ans 
        if num1_curr:
            product1 = multiplier * num1_curr.data
            ans += product1
            num1_curr = num1_curr.next
        if num2_curr:
            product2 = multiplier * num2_curr.data
            ans += product2
            num2_curr = num2_curr.next 
        # multiply multiplier by ten with
        # every iteration 
        multiplier *= 10 

    digit = None 
    output = None 

    multiplier /= 10 
    while ans != 0:
        digit = ans / multiplier 
        node = linkedList.Node(digit)
        if output is None:
            output = node 
        else: 
            node.next = output 
            output = node 
        ans %= multiplier
        multiplier /= 10 

    return output

num1 = linkedList.SLinkedList()
num1.Atbeginning(6)
num1.Atbeginning(1)
num1.Atbeginning(7)
print('num 1')
num1.LListprint()
print('')

num2 = linkedList.SLinkedList()
num2.Atbeginning(2)
num2.Atbeginning(9)
num2.Atbeginning(5)
print('num 2')
num2.LListprint()

ans = sumLists(num1.head, num2.head)

print('')
ans_str = ''

curr = ans 
while curr: 
    ans_str += str(curr.data)
    ans_str += ' '
    curr = curr.next

print('ans')
print(ans_str)