class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge_sort(arr):
            n = len(arr)
            
            if n == 2:
                if arr[0] < arr[1]:
                    return arr
                else: 
                    return [arr[1], arr[0]]
            elif n < 2:
                return arr
            
            arr1 = merge_sort(arr[:n//2])
            arr2 = merge_sort(arr[n//2:])

            # combine arrays
            arr3 = []

            lp, rp = 0, 0

            while lp < len(arr1) or rp < len(arr2):
                if lp < len(arr1):
                    if rp < len(arr2):
                        if arr1[lp] <= arr2[rp]: 
                            arr3.append(arr1[lp])
                            lp += 1
                        else:
                            arr3.append(arr2[rp])
                            rp += 1
                    else:
                        arr3.append(arr1[lp])
                        lp += 1
                else:
                    arr3.append(arr2[rp])
                    rp += 1


            return arr3

        
        return merge_sort(nums)
