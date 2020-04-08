class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        G = set(G)
        count = 0
        while head:
            if head.val in G:
                while head.next and head.next.val in G:
                    head = head.next
                count += 1
            head = head.next
            
        return count