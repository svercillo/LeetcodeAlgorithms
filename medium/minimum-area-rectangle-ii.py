class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        n = len(points)
        points.sort()


        ppl = defaultdict(list)

        for i in range(n-1):
            for j in range(1,n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                if y2 > y1 or points[i] == points[j]:
                    continue

                if x2 - x1 ==  0: 
                    m = math.inf
                else:
                    m = (y2  - y1) / (x2 - x1)

                b = y1 - x1 * m
                m = round(m, 5) if m < math.inf else m
                
                ppl[m].append((points[i], points[j]))

    

        def formrectangle(line1, line2):
            (x1, y1), (x2, y2) = line1
            (x1b, y1b), (x2b, y2b) = line2

            if x2 - x1 == 0:
                m = math.inf
            else: 
                m = (y2  - y1) / (x2 - x1)
            m = round(m, 5) if m < math.inf else m

            if y2 - y1 == 0:
                invm = math.inf
            else:
                invm = -(x2 - x1) / (y2  - y1)

            if (x1b - x1) == 0:
                foundinvm = math.inf
            else:
                foundinvm = (y1b - y1) / (x1b - x1)

            if invm == foundinvm:
                return True 
            return False

        def linelength(line1):
            (x1, y1), (x2, y2) = line1
            return math.sqrt(abs(x2 - x1) ** 2 + abs(y2 - y1) ** 2)


        def area(line1, line2):
            (x1, y1), (x2, y2) = line1
            (x1b, y1b), (x2b, y2b) = line2


            linelen = linelength(line1)
            linelen2 = linelength(line2)
            perplinelen = linelength(((x1, y1), (x1b, y1b)))
            perplinelen2 = linelength(((x2, y2), (x2b, y2b)))

            if linelen != linelen2 or perplinelen != perplinelen2:
                return 0
            return linelen * perplinelen



        a = area(
            ([0, 1], [1, 0]),
            ([1, 2], [2, 1])
        )


            
        minarea = math.inf
        for m in ppl:
            possible = ppl[m]
            for line1ind in range(len(possible)):
                for line2ind in range(len(possible)):
                    line1 = possible[line1ind]
                    line2 = possible[line2ind]

                    if formrectangle(line1, line2): 
                        a = abs(area(line1, line2))
                        print("considering ", line1, line2, a) 
                        if 0< a < minarea:
                            minarea = a
        return minarea if minarea < math.inf else 0
