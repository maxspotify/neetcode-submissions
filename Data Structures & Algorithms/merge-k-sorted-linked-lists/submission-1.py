# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge_lists(list1, list2):
            dummy = ListNode()
            tail = dummy

            while list1 and list2:
                if list1.val >= list2.val:
                    tail.next = list2
                    list2 = list2.next
                else:
                    tail.next = list1
                    list1 = list1.next
                tail = tail.next
            
            if list1:
                tail.next = list1
            if list2:
                tail.next = list2
            
            return dummy.next

        if not lists:
            return None

        while len(lists) > 1:
            merged = []
            for i in range(0, len(lists), 2):
                merged_list = merge_lists(lists[i], lists[i+1] if i+1 < len(lists) else None)
                merged.append(merged_list)
            lists = merged


        return lists[0]

            