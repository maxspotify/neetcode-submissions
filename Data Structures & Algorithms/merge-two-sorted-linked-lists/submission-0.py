# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        result = None
        if list1.val <= list2.val:
            result = ListNode(val=list1.val)
            list1 = list1.next
        else:
            result = ListNode(val=list2.val)
            list2 = list2.next
        
        tracker = result
        
        while (list1 and list2):
            if list1.val <= list2.val:
                tracker.next = ListNode(val=list1.val)
                tracker = tracker.next
                list1 = list1.next
            else:
                tracker.next = ListNode(val=list2.val)
                tracker = tracker.next
                list2 = list2.next
        if list1:
            tracker.next = list1
        else:
            tracker.next = list2
        return result

