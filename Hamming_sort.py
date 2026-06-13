def solve (N, K, A):
    # Write your code here
    A.sort(key = lambda x : ((x^K).bit_count(), x))
    return A
