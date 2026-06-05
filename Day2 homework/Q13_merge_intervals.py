def merge(intervals):
        intervals.sort()
        ans = []
        prev = intervals[0]
        for i in range(1, len(intervals)):
            if prev[1] >= intervals[i][0]:
                prev[1] = max(prev[1], intervals[i][1])
            else:
                ans.append(prev)
                prev = intervals[i]
        ans.append(prev)
        return ans
