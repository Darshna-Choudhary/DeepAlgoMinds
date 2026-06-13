def powerSum(X, N):
    # Write your code here
    def calc(rem, n):
        power = n ** N
        if rem == 0:
            return 1
        if power > rem:
            return 0
        
        take = calc(rem - power, n+1)
        skip = calc(rem, n+1)
        
        return take + skip
    return calc(X, 1)
