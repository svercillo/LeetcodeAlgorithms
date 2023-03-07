def gcd(a, b):
    # Input: Two integers a and b, where a  b  0
    # Output: Integer d such that d = gcd(a, b) and ax + by = d
    if b == 0:
        return a
    d = gcd(b, a % b)
    return d