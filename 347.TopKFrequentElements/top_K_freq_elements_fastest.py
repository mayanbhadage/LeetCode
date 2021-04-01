class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counter = Counter(nums)
        
        result = []
        inverse_counter = defaultdict(list)
        # The idea is the num will have max freq of len(nums)
        for key, value in counter.items():
            inverse_counter[value].append(key)
        
        
        for idx in range(len(nums), 0, -1):
            if idx in inverse_counter:
                result.extend(inverse_counter[idx])
                if len(result) >= k:
                    break
        return result