#l1 = [2,4,3]
#l2 = [5,6,4]
#o/p = 7 0 8 
#Explanation: 342 + 465 = 807.

#Definition for singly-linked list.
from typing import Optional
 class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next  # Add next pointer

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None and l2 is None:
            return None

        current = ListNode()
        root = current
        rem = 0
        prev = None

        while True:
            if not l1 and not l2:
                if rem:
                    sum = ListNode(val=rem)
                    prev.next = sum
                return root
          
            if prev:  
                prev.next = current
                
            sum = rem
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
    
            rem = 1 if sum > 9 else 0
            current.val = sum if sum < 10 else sum - 10

            prev = current
            current = ListNode()

def list_to_linked_list(lst):
    head = None
    for val in lst[::-1]:  # Iterate in reverse to build from tail
        head = ListNode(val, head)
    return head
    
def print_linked_list(node):
    while node:
        print(node.val, end=" ")
        node = node.next
    print()

l1 = [2,4,3]
l2 = [5,6,4]
sol=Solution()
l1=list_to_linked_list(l1)
l2=list_to_linked_list(l2)
result = sol.addTwoNumbers(l1,l2)
print_linked_list(result)

###############
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        op = opHead = ListNode()
        s = 0

        while l1 or l2 or s:
            op.next = ListNode()
            op = op.next

            s += (l1.val if l1 else 0) + (l2.val if l2 else 0)
            s, op.val = divmod(s, 10)

            l1 = l1.next if l1 else False
            l2 = l2.next if l2 else False

        return opHead.next
