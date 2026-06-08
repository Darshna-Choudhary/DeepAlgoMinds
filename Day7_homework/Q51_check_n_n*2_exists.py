def checkIfExist(arr):
        seen = set()
        for i in arr:
            if i*2 in seen or i/2 in seen:
                return True
            seen.add(i)
        return False
