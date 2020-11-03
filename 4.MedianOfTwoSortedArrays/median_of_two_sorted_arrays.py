class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        x = len(nums1)
        y = len(nums2)
        even = (x + y) % 2 == 0
        left = 0
        right = x
        
        while(left <= right):
            part_x = (left + right)//2
            part_y = (x + y +1)//2 - part_x
            #print(part_x, part_y)
            
            x1 = -math.inf if part_x == 0 else nums1[part_x-1]
            x2 =  math.inf if part_x == x else nums1[part_x]
            
            y1 = -math.inf if part_y == 0 else nums2[part_y - 1]
            y2 = math.inf if part_y == y else nums2[part_y]
            #print("x1: {}\nx2: {}\ny1: {}\ny2: {}\n\n".format(x1, x2, y1, y2))
            if x1 <= y2 and y1 <= x2:
                #print("Here")
                if even:
                    return((max(x1,y1) + min(x2,y2))/2)
                else:
                    return max(x1,y1)
            elif x1 > y2:
                right= part_x - 1
            else:
                left = part_x + 1
        
                