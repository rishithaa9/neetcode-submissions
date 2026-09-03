# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy=ListNode()
        dummy.next=head
        curr=head
        count=0
        while curr:
            curr=curr.next
            count+=1

        target=count-n
        curr=dummy
        for _ in range(target):
            curr=curr.next
        curr.next=curr.next.next

        return dummy.next


        
