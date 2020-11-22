class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        hmap_pos = {"UP": (0,1),"DOWN":(0,-1),"LEFT":(-1,0), "RIGHT":(1,0)}
        hmap_left = {"UP": "LEFT","DOWN":"RIGHT","LEFT":"DOWN", "RIGHT":"UP"}
        hmap_right = {"UP": "RIGHT","DOWN":"LEFT","LEFT":"UP", "RIGHT":"DOWN"}
        
        pos = [0,0]
        dir_ = "UP"
        
        for i in range(4):
            pos, dir_ = self.simulate(instructions, pos, dir_, hmap_pos, hmap_left,hmap_right)
            if pos == [0,0]:
                return True
            #print(pos)
        return False
        
        
    def simulate(self, instructions, pos, direction, hmap_pos, hmap_left, hmap_right):
        for instruction in instructions:
            if instruction == "G":
                X = pos[0] + hmap_pos[direction][0]
                Y = pos[1] + hmap_pos[direction][1]
                pos = [X, Y]
            elif instruction == "L":
                direction = hmap_left[direction]
            else:
                direction = hmap_right[direction]
        return (pos, direction)
                    
