class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x, y = 0, 0
        dir = 0
        moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for instr in instructions:
            if instr != "R" and instr != "L":
                dx, dy = moves[dir % 4]
                x += dx
                y += dy
            elif instr == "R":
                dir += 1
            else:
                dir -= 1
        return (x == 0 and y == 0) or dir % 4 != 0
