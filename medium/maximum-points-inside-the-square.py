class Solution:
    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:
        tagBy = {}
        
        for i, coords in enumerate(points):
            tagBy[tuple(coords)] = s[i]

        points.sort(key = lambda k : max(abs(k[0]), abs(k[1])))
        

        broken_len = None
        broken_ind = None
        
        tag_set = set()
        for i, point in enumerate(points):
            tag = tagBy[tuple(point)]
            if tag in tag_set:
                broken_len = max(abs(point[0]), abs(point[1]))
                broken_ind = i
                break
            tag_set.add(tag)

        if broken_len is None: 
            return len(points)
        
        while i >= 0 and max(abs(points[i][0]), abs(points[i][1])) == broken_len:
            i -= 1
        
        return i + 1
