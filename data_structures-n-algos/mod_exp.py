
# x ** y % N
def mod_exp(x,y, N):

    if y == 0: 
        return 1

    z = mod_exp(x, y//2, N)

    if y % 2 ==0: 
        return z * z % N
    else:
        return x * z * z % N

print(mod_exp(2, 5, 7))