class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = defaultdict(int)
        for num in nums:
            hmap[num] += 1
        heap = []
        
        for key, value in hmap.items():
            if len(heap) < k:
                heapq.heappush(heap,(value, key))
            else:
                V, K = heap[0]
                if V < value:
                    heapq.heapreplace(heap, (value,key))
        return [k for v,k in heap]