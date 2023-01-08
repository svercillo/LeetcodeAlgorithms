class Solution(object):
    def makeConnected(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        uf = [-1] * n
        
        if len(connections) < n-1:
            return -1
    
        for l, r in connections:
            l, r = sorted([l,r])
            
            
            prim_l = l
            while uf[prim_l] != -1:
                prim_l = uf[prim_l]
            
            prim_r = r
            while uf[prim_r] != -1:
                prim_r = uf[prim_r]
    
            if prim_l != prim_r:
                uf[prim_r] = prim_l
        
        dis_joint = 0
        for c in uf:
            if c == -1:
                dis_joint +=1
                
        print(dis_joint,uf )
        
        if len(connections) >= dis_joint - 1:
            return dis_joint -1
        else:
            return -1 
            
