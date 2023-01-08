class SnapshotArray:

    snapshots = [{}]
    ind = 0 
    def __init__(self, length: int):
        self.array = [0] * length
    
    def set(self, index: int, val: int) -> None:
        self.snapshots[self.ind][index] = val
        

    def snap(self) -> int:
        self.snapshots.append({})
        self.ind += 1
        return self.ind -1 
        

    def get(self, index: int, snap_id: int) -> int:
        
        for i in range(snap_id, -1, -1):
            if index in self.snapshots[i]:
                return self.snapshots[i][index]
        
        return 0
            
            
                
            
        
