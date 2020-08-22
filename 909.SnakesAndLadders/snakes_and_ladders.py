class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        
        
        N = len(board)
        
        
        queue = deque([(1,0)])
        
        visited = set()
        steps = 0
        
        while queue:
            curr_pos,steps = queue.popleft()
            
            if curr_pos == N*N:
                return steps
            
            if curr_pos not in visited:
                visited.add(curr_pos)
                for move in range(1,7):
                    new_pos = curr_pos + move
                    if new_pos > N * N:
                        continue
                    cordinates = self.calculate_position(new_pos, N)
                    row, col = cordinates
                    if board[row][col] != -1:
                        queue.append((board[row][col],steps+1))
                    else:
                        queue.append((new_pos,steps+1))
        
        return -1
        
        
    def calculate_position(self,num, N):
         # for row:
        row = -1
        col = -1
        if num % N == 0:
            row = N - num//N
        else:
            row = N - num//N - 1
        
        # For col, If both row and N are odd or both row and N are even : reverse the col
        col = (num - 1) % N
        
        if row % 2 == N % 2:
            col = N - 1 - col
        
        return (row,col)
            
        