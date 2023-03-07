def get_largest_element_smaller_than_x(arr, x):
    n = len(arr)
    lp, rp = 0, n - 1

    while lp <= rp: 
        m = (lp+rp) // 2

        if arr[m] < x:
            lp = m + 1
        else:
            rp = m - 1
    
    def check_index(ind):
        if arr[ind] < x and (ind + 1 == len(arr) or  arr[ind + 1] >= x):
            return True
    
    if lp == n:
        lp -= 1
    
    if check_index(lp): return lp
    if check_index(lp + 1): return lp + 1
    if check_index(lp - 1): return lp -1

    return -1



arr = [1,1,1,1,1,1]
res = get_largest_element_smaller_than_x(arr, float(input()))

print(res)
print(arr[res])


    
# def test_get_closest_smaller_element():
#     # Test case 1
#     arr = [1, 3, 4, 6, 8]
#     x = 5
#     assert get_closest_smaller_element(arr, x) == 2

#     # Test case 2
#     arr = [1, 3, 4, 6, 8]
#     x = 0
#     assert get_closest_smaller_element(arr, x) == -1

#     # Test case 3
#     arr = [1, 3, 4, 6, 8]
#     x = 10
#     print(get_closest_smaller_element(arr, x))
#     assert get_closest_smaller_element(arr, x) == 4

#     # Test case 4
#     arr = [1, 1, 1, 1, 1]
#     x = 1
#     assert get_closest_smaller_element(arr, x) == -1

#     # Test case 5
#     arr = [1, 3, 5, 7, 9]
#     x = 3
#     assert get_closest_smaller_element(arr, x) == 0

#     # Test case 6
#     arr = [1, 3, 5, 7, 9]
#     x = 2
#     assert get_closest_smaller_element(arr, x) == 0





# test_get_closest_smaller_element()