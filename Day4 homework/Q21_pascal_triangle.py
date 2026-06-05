def generate(numRows):
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        
        prevrows = self.generate(numRows-1)
        prevrow = prevrows[-1]
        newrow = [1]

        for i in range(1, numRows-1):
            newrow.append(prevrow[i-1] + prevrow[i])
        newrow.append(1)
        prevrows.append(newrow)
        return prevrows
