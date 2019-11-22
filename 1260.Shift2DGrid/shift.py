class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m_list = []
        r = len(grid)
        c = len(grid[0])
        for List in grid:
            for val in List:
                m_list.append(val)
                
        temp = m_list
        for i in range(0,k):
            value = temp[-1]
            value2 = temp[:-1]
            temp = []
            temp.append(value)
            temp.extend(value2)

        result = []
        for i in range(0,r):
            ll = []
            for j in range(0,c):
                ll.append(temp[j])
            temp = temp[c:]
            result.append(ll)
        return (result)