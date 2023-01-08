# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    
    results = list()
    p = 0
    def __init__(self, nestedList):
            
        def dfs(obj):
            if obj.isInteger():
                self.results.append(obj.getInteger())
            else:
                arr = obj.getList()
                for ele in arr:
                    dfs(ele)        
            
        for ele in nestedList:
            dfs(ele)
        
        print(self.results)
                

    def next(self):
        res = self.results[self.p]
        self.p += 1
        return res 
    
    def hasNext(self):
        return self.p < len(self.results)
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
