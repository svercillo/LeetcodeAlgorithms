class Solution:
    def racecar(self, target: int) -> int:
        # idea: bfs, cache on speed and position 


        length = 0
        q = [(0, 1)]

        visited = set()
        while q:
            new_q = []
            for pos, speed in q:

                if pos == target:
                    print(pos, speed)
                    print("HEHEHEHE")
                    return length
                if (pos, speed) in visited:
                    continue

                visited.add((pos, speed))

                new_q.append((pos + speed, speed * 2))
                if speed > 0:
                    new_q.append((pos, -1))
                else:
                    new_q.append((pos, 1))
            q = new_q

            # q.sort(key=lambda k : abs(target - k[0]))

            length += 1

        return length
