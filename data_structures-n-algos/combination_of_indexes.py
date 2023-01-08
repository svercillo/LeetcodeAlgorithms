array = [1,2,3,4,5]
n = len(array)

def generate_combination_of_indexes(n):
    combs = [] 
    last_row = [[]]
    for _ in range(3):
        next_row = []
        for ele in last_row:

            if len(ele) > 0:
                last = ele[-1]
            else:
                last = -1

            for j in range(last +1, n):
                old_list = ele.copy()
                old_list.append(j)
                
                next_row.append(old_list)
                # print(old_list, next_row)
        

        combs.extend(last_row)
        last_row = next_row.copy()
    combs.extend(last_row)

    return combs


print(generate_combination_of_indexes(12))