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


# nums = [0, 5, 10, 15, 20, 25, 30]

# print("Enter target .. ")
# target = int(input())
# res1, _ = binary_search(nums, target)
# print(res1)
# print("enter target 2 ")
# target = int(input())
# res2, _ = binary_search(nums, target)
# print(nums[res1:res2+1])

# nums.insert(res, target)
# print(nums)
