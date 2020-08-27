class Solution:
    def canCross(self, stones: List[int]) -> bool:
        set_stones = set(stones)
        target = stones[-1]
        self.success = False
        pos = 0
        jump = 1
        
        if pos + jump not in set_stones:
            return False
        stack = deque([(pos,jump)])
        seen = set()
        while stack:
                
            pos, jump = stack.pop()

            current_pos = pos + jump
            if current_pos == target:
                return True

            for move in [-1, 0, 1]:
                next_jump = jump + move


                next_pos = current_pos + next_jump

                if 0 <= next_pos <= target and next_pos in set_stones:
                    if next_jump != 0 and (current_pos, next_jump) not in seen:
                        stack.append((current_pos, next_jump))
                        seen.add((current_pos, next_jump))