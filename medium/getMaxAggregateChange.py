def getMaxAggregateChange(changes: list):
    prefix, suffix = [], []
    
    _sum = 0
    for n in changes:
        _sum += n
        prefix.append(_sum)

    _sum = 0
    for n in changes[::-1]:
        _sum += n
        suffix.append(_sum)

    suffix = suffix[::-1]

    print(prefix)
    print(suffix)
    
    max_change = prefix[0]

    n = len(changes)
    for i in range(0,n):

        max_change = max(max_change, max(prefix[i], suffix[i-1]))

    return max_change
