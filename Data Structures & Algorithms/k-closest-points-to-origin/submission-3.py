class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance_cal (x,y):
            return math.sqrt((x)**2 + (y)**2)
        
        heap= []

        for x,y in points:
            key = (x,y)
            heapq.heappush(heap,(distance_cal(x,y),key))
        
        print (heap[:])
        res = []
        for _ in range(k):
            distance,key = heapq.heappop(heap)
            res.append(key)

        return res