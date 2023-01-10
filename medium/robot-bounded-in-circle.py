class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        
        n = len(instructions)

        visited = {}  # ((coords), instruction_ind): iteration
        instr_ind = 0
        i, j = 0,0
        directions = [[0,1], [1,0], [0,-1], [-1,0]]
        dind = 1000 * 4

        while instr_ind < 4 * n + 4:
            iteration = instr_ind // 4
            

            key = ((i, j), instr_ind % n)
            if key not in visited:
                visited[key] = set()
            
            visited[key].add(iteration)
            for _iteration in range(4):
                if _iteration == iteration:
                    continue
                if _iteration in visited[key]: # different iteration has same instruct at same position
                    print(visited)
                    return True

            # print(i, j, iteration, instr_ind)
            match instructions[instr_ind % n]:
                case "G":
                    down, right = directions[dind  % 4]
                    i = i + down
                    j = j + right
                case "L":
                    dind -= 1
                case "R":
                    dind += 1

            instr_ind += 1

        # print(visited)
        return False
