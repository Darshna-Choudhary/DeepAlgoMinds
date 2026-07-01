class Solution:
    def __init__(self):
        self.count = 0
    def  towerOfHanoi(self, n, fromm, aux, to):
        # code here
        if n == 0:
            return
        self.towerOfHanoi(n-1, fromm, to, aux)
        self.count += 1
        self.towerOfHanoi(n-1, aux, fromm, to)
        return self.count
