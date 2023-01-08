# A Python program to print all
# permutations using library function
import itertools
 
# Get all permutations of [1, 2, 3]
perm = itertools.permutations([1, 2, 3])
 
# Print the obtained permutations
# for i in list(perm):
#     print (i)




def permutations_of_indexes(n):
    perms = []
    last_row = [[]]

    for i in range(n +1):

        next_row = []
        for ele in last_row: 
            for j in range(0, n): 
                old_list = ele.copy()
                old_list.append(j)
            

                next_row.append(old_list)

        perms.extend(last_row)

        last_row = next_row.copy()

    perms.extend(last_row)

    return perms

res = permutations_of_indexes(3)

print(res)


    


    
