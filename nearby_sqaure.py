n1 = len(arr)
def calc_diff(arr, bsum, csum, i):
    if i == n1:
        return abs(bsum*bsum - csum*csum)
    return min(calc_diff(arr, bsum+arr[i], csum, i+1),
        calc_diff(arr, bsum, csum+arr[i], i+1))
print(calc_diff(arr, 0, 0, 0))
