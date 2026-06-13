def add(n):
    if n < 10:
        return n
    ans = 0
    while n > 0:
        ans += (n % 10)
        n = n // 10
    return add(ans)


def superDigit(n, k):
    # Write your code here
    n = sum(int(ch) for ch in n) * k
    return add(n)
