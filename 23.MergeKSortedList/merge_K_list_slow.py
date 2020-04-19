# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        while(len(lists) != 1):
            list1 = lists.pop()
            list2 = lists.pop()
            new_list = self.merge_two_list(list1, list2)
            lists.append(new_list)
        
        return lists[0]
        
    
    def merge_two_list(self, list1, list2):
        dummy = curr = ListNode(0)
        
        while(list1 and list2):
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
            
        curr.next = list1 or list2
        
        return dummy.next
        