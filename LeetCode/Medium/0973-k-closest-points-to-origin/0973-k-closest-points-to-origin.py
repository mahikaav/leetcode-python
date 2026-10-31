class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        heap = [] 

        for p in points:
            dist = math.sqrt(p[0]**2 + p[1]**2)
            
            if len(heap) < k:
                heapq.heappush(heap, (-dist,p))
            elif dist < -heap[0][0]:
                heapq.heappushpop(heap, (-dist,p))
        
        ans = [pair[1] for pair in heap]
        return ans

        
        