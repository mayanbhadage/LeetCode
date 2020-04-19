class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = []
        
        for list_ in lists:
            
            while list_:
                heapq.heappush(heap, list_.val)
                list_ = list_.next
        
        dummy = curr = ListNode(0)
        while(heap):
            curr_val = heapq.heappop(heap)
            newNode = ListNode(curr_val)
            curr.next = newNode
            curr = curr.next
        
        return dummy.next