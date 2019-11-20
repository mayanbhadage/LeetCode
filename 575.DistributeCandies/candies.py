class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        return int(min(len(set(candies)),len(candies)/2))