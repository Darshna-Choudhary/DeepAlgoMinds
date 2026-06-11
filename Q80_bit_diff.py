def countBitsFlip(a, b):
        #code here
        ans = a ^ b
        count = 0
        while ans > 0:
            ans = ans & (ans-1)
            count += 1
        return count
