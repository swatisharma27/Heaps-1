import heapq
class Solution:
    def findKthLargest(self, nums, k):
        """
        TC: O(n * log k)
        AS: O(k)
        """
        pq = [] # min heap

        for num in nums:
            heapq.heappush(pq, num)
            if len(pq) > k:
                heapq.heappop(pq)

        return pq[0] 
