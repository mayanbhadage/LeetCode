class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hmap = {}
        for value in arr:
            if value in hmap:
                hmap[value] +=1
            else:
                hmap[value] = 1
        unique_set = set(hmap.values())
        unique_list = list(unique_set)
        h_values = list(hmap.values())
        unique_list.sort()
        h_values.sort()

        
        return h_values == unique_list