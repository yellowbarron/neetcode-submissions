class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        timemap = {i:[] for i in range(1,n+1)}
        for src,target,time in times:
            timemap[src].append((target,time))
        
        heap = [(0,k)]
        
        time = 0
        signal = set()

        while heap:
            w1, n1 = heapq.heappop(heap)
            if n1 in signal:
                    continue
            
            signal.add(n1)
            time = max(w1,time)

            if n1 in timemap:
                for n2, w2 in timemap[n1]:
                    if n2 not in signal:
                        heapq.heappush(heap,(w1+w2,n2))
        
        return time if len(signal) == n else -1
            
            


            

        





        