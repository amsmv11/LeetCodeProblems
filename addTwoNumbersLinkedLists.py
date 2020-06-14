# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        total_sum = 0
        CounterDecimal = 0
        while l1 != None:
            total_sum += l1.val * (10**CounterDecimal)
            CounterDecimal += 1
            l1 = l1.next
        CounterDecimal = 0    
        while l2 != None:
            total_sum += l2.val * (10**CounterDecimal)
            CounterDecimal += 1
            l2 = l2.next
        lres = ListNode()
        previous = None
        for e in range(len(str(total_sum))):
            if previous == None:
                lres.val = total_sum%10
                previous = lres
            else:
                newRes = ListNode()
                newRes.val = total_sum%10
                previous.next = newRes
                previous = newRes
            total_sum = total_sum//10

        return lres