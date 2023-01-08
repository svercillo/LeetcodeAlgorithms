class Solution:
    def findLucky(self, arr) -> int:
        arr.sort()
        
        # print(arr)
        
        lucky_num = -1
        i = 0
        while i < len(arr):
            # print(i)
            lucky = True
            
            start = i
            end = i + arr[i]
            if end > len(arr):
                # print(start, end)
                break

            count =0 
            for k in range(start, end):
                if arr[k] == arr[i]:
                    count +=1


            l = end
            while l < len(arr) and arr[l] == arr[i]:
                count +=1 
                end +=1 
                l +=1 



            if count ==arr[i]:
                lucky_num = arr[i]
                

            i += count

                
        
        

        print(lucky_num )
        return lucky_num
