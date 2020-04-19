class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        #See the Pattern
        N = N % 14
        if N == 0:
            N = 14
            
        hmap = {}
        for _ in range(N):
            cells = self.change_state(cells,hmap)
        return cells
        
        
        
        
    def change_state(self, cells,hmap):
        t = tuple(cells)
        if t in hmap:
            return hmap[t]
        else:
            
            new_cells = [0] * len(cells)
            for i in range(1, len(cells)-1):
                if cells[i-1] == cells[i+1]:
                    new_cells[i] = 1
            hmap[t] = new_cells
            return new_cells