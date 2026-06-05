def findKthLargest(nums, k):
    heap = []
    for i in nums:
        heapq.heappush(heap, i)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]

nums = [3, 2, 1, 5, 6, 4]
k = 2
print(findKthLargest(nums, k))
# Output: 5
