class SegTree:

    def __init__(self, nums):
        self.n = 2 ** ceil(log(len(nums),2))
        self.tree = [0] * (self.n * 2)
        tree = self.tree

        
        for i,e in enumerate(nums):
            self.update(i, e)

        for ind in range(self.n-1, -1, -1):
            tree[ind] = max(tree[2 * ind], tree[2*ind+ 1])

    def update(self, ind, value): 
        tree = self.tree
        tree[ind + self.n] = value

        ind += self.n

        while ind > 0: 
            ind //= 2
            tree[ind] = max(tree[2*ind], tree[2*ind + 1])
        # # # print("update", ind,value, tree)
        

    def findleftmostgte(self, target):
        p = 1
        
        tree = self.tree
        if tree[p] < target: 
            return -1

        while 2* p < len(tree) and tree[p] >= target:
            if tree[2*p] >= target:  #try the left child first always -> else go rights
                p += p 
            else:
                p += p + 1

        
 
            
        # # # print("\tFound", target, self.tree[self.n:p+1], self.tree[p])
        if self.tree[p] < target:
            return -1

        return p - self.n
        

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        segtree = SegTree(baskets)

        

        unplaced = 0
        for i, f in enumerate(fruits):
            ind = segtree.findleftmostgte(f)
            # # print("finding bset", ind, f,)
            
            if ind == -1:
                unplaced += 1
            else:    
                baskets[ind] = 0
                segtree.update(ind, baskets[ind])
        
        return unplaced
