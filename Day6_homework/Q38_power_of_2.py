def isPowerOfTwo(n):
        if n == 0:
            return False
        b = bin(n)[2:]
        lb = list(b)
        for i in range(1, len(lb)):
            if lb[0] != '1' or lb[i] != '0':
                return False
        return True


def isPowerOfTwo(n):
        if n == 0:
            return False
        if n & (n - 1) == 0:
            return True
        else:
            return False
