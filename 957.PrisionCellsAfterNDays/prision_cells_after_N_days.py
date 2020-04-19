class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        for _ in range(N):
            
            self.change_state(cells)
        return cells
        
     def change_state(self, cells):
        prev = None
        ptr1 = 0
        for i in range(1, len(cells)-1):
            if cells[i-1] == cells[i+1]:
                curr = 1
            else:
                curr = 0
            if ptr1 > 0:
                cells[ptr1] = prev
            prev = curr
            ptr1 += 1
        cells[ptr1] = prev
        cells[ptr1 + 1] = 0 