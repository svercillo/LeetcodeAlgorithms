from bisect import bisect, bisect_right, bisect_left

nums = [0, 2, 3, 3]
# print("enter target")
# target = float(input())

# # res = bisect(nums, target)
# res = bisect_left(nums, target, 0, len(nums))
# print(res, nums[res])


# nums.insert(res, target)
# print(nums)




def binary_search(array, target):
    if len(array) == 0:
        return -1, False

    n = len(array)
    l, r = 0, n - 1

    while l <= r:
        m = (l + r) // 2

        if array[m] == target:
            l = m
            break
        elif array[m] > target:
            r = m - 1
        else:
            l = m + 1

    if l == n:
        return n

    while array[l] >= target and l >= 0:
        l -= 1

    if l + 1 < len(array) and array[l + 1] == target:
        return l + 1

    return l



# def binary_search(array, target):
#     n = len(array)

#     l, r = 0, n-1 

#     while l <= r: 
#         m = (l + r) // 2
        

#         if array[m] == target:
#             return m
        
#         elif array[m] > target:
#             r = m - 1
#         else:
#             l = m + 1


    
#     while l >= 0 and array[l] > target:
#         l -=1

#     return l


arr = [-1, 0, 3, 5, 9, 10]
ind = binary_search(arr, -2)


print(ind)








# print(ind, arr[ind])






def rev_binary_search(array, target):
    if len(array) == 0:
        return -1, False

    n = len(array)
    l, r = 0, n - 1

    while l <= r:
        m = (l + r) // 2

        if array[m] == target:
            l = m
            break
        elif array[m] < target:
            r = m - 1
        else:
            l = m + 1

    if l == n:
        return n

    while array[l] <= target and l >= 0:
        l -= 1

    if l + 1 < len(array) and array[l + 1] == target:
        return l + 1
    else:
        return l



# find the first index 'i'  where array[i] >= target
def binary_search(array, target):
    if len(array) == 0:
        return -1
    elif len(array) == 1:
        return 0 if array[0] >= target else 1
    
    n = len(array)
    l, r = 0, n - 1
    
    while l <= r:
        mid = (l +r) // 2
        print(mid, l,r)
        if mid == 0:
            # (l,r) = (0,1)
            if array[0] >= target:
                return 0
            elif array[0] < target:
                if array[1] < target:
                    return 2
                elif array[1] >= target:
                    return 1        
        
        if array[mid-1] < target and array[mid] >= target: 
            return mid
        if array[mid -1] < target and array[mid] < target:
            l = mid + 1
        elif array[mid-1] >= target:
            r = mid - 1
    
    if l == 0:
        # (l,r) = (0,1)
        if array[0] > target:
            return 0
        else:
            if array[1] < target:
                return 1
            else:
                return 2
    else:
        if l  == len(array):
            return len(array)
        if array[l-1] < target and array[l] >= target: 
            return l
        elif array[l -1] < target and array[l] < target:
            return l + 1
        elif array[l-1] >= target:
            return  l -1
        
        
        
def binary_search(array, target):
    n = len(array)
    
    if n == 1:
        return 0 if array[0] >= target else 1
    
    l, r = 0, n - 1          
    while l <= r:
        m = (l + r) // 2
        if m == 0:
            if array[0] >= target: 
                return 0
            elif array[1] >= target: 
                return 1
            else: 
                return 2
    
        if array[m-1] < target:
            if array[m] >= target:         
                return m
            else:
                l = m + 1
        else:
            r = m - 1
    
    if m == 0:
        if array[0] >= target: 
            return 0
        elif array[1] >= target: 
            return 1
        else: 
            return 2

    
    l = m
    if array[m-1] < target:
        if array[m] >= target:         
            return m
        else:
            return m + 1
    else:
        return m -1

    
        
# def binary_search(array, target):
#     n = len(array)
#     l, r = 0, n-1
    
#     while l <=r:
    
#         mid = (l + r) // 2 
        
        
#         if mid == 0:
#             if array[0] < target:
#                 return 1
#             elif array[0] > 
            
#         if array[mid-1] 


# def binary_search(array, target):
#     if len(array) == 0:
#         return -1

#     n = len(array)

#     l, r = 0, n - 1

#     while l <= r:
#         m = (l + r) // 2

#         if array[m] == target:
#             return m
#         elif array[m] > target:
#             r = m - 1
#         else:
#             l = m + 1

#     if l == n:
#         return n - 1

#     while array[l] > target and l > 0:
#         l -= 1
#     return l

# [[1, 5]]


# nums = [0,0,5,5,5,5,5, 7,7,7,7, 10]
nums = [0,12]

print("Enter target .. ")
target = int(input())
res1 = binary_search(nums, target)
print(res1)
# print("enter target 2 ")
# target = int(input())
# res2, _ = binary_search(nums, target)
# print(nums[res1:res2+1])

# nums.insert(res, target)
# print(nums)
