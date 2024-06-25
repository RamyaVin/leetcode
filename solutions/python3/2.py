# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
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
