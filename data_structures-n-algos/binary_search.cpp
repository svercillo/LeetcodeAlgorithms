pair<int, bool> binary_search(vector<int> array, int target){

    if (array.size() == 0){
        return make_pair(-1, false);
    }

    int n = array.size():

    int l = 0;
    int r = n -1;

    while (l <= r){
        int m = (l + r) / 2;

        if (array[m] == target){
            return make_pair(m, true);
        } else if (array[m] > target){
            r = m -1;
        } else{ 
            l = m + 1;
        }
    }

    if (l == n)
        return make_pair(n -1, false);

    while (l >= 0 && arr[l] > target)
        l -= 1;
    
    return make_pair(l, false);
}




[[
    [0,0,1,1,2],
    [0,67,69,74,87]],
    
    
    [4],[62],[100],[88],[70],[73],[22],[75],[29],[10]]

// def binary_search(array, target):
//     if len(array) == 0:
//         return None, False

//     n = len(array)
//     l, r = 0, n - 1

//     while l <= r:
//         m = (l + r) // 2

//         if array[m] == target:
//             return m, True
//         elif array[m] > target:
//             r = m - 1
//         else:
//             l = m + 1

//     if l == n:
//         return n - 1, False
//     while array[l] > target and l >= 0:
//         l -= 1

//     return l, False