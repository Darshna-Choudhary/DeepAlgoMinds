class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        ans = letters[0]
        st = 0; end = len(letters) - 1
        while st <= end:
            mid = st + (end - st) // 2
            if letters[mid] > target:
                ans = letters[mid]
                end = mid - 1
            else:
                st = mid + 1
        return ans