# Definition for singly-linked list.

import heapq
from typing import List, Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


    def __lt__(self, other):
        return self.val < other.val


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        TC: O(N log k); N = number of nodes(n) * number of linked lists (k)
        AS: O(k)
        """

        min_heap = []

        # Add heads to each of the lists
        for l in lists:
            if l:
                heapq.heappush(min_heap, l)
    
        dummy = ListNode()
        curr = dummy

        while min_heap:
            smallest = heapq.heappop(min_heap)
            curr.next = smallest
            curr = curr.next
            if smallest.next:
                heapq.heappush(min_heap, smallest.next)

        return dummy.next
