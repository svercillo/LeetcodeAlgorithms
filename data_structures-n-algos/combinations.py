import itertools

stuff = [1, 2, 3]


def combinations(array):
    combs = list()
    for L in range(len(array) + 1, -1, -1):
        for subset in itertools.combinations(array, L):
            combs.append(subset)

    return combs


res = combinations(stuff)
print(res)
