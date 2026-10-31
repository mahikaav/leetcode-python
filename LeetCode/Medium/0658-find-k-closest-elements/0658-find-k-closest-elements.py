class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []

        for n in arr:
            dist = abs(x - n)
            if len(heap) < k:
                heapq.heappush(heap, (-dist,n))
            elif dist < -heap[0][0]:
                heapq.heappushpop(heap,(-dist,n))
        
        ans = [pair[1] for pair in heap]
        ans.sort()
        return ans