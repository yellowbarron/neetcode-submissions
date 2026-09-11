class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre_map = { i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            pre_map[crs].append(pre)


        visit = set()
        res = []
        def dfs(crs):
            if pre_map[crs] == []:
                if crs not in res:
                    res.append(crs)
                return True
            
            if crs in visit:
                return False
            
            visit.add(crs)

            for pre in pre_map[crs]:
                if not dfs(pre):
                    return False
            
            visit.remove(crs)
            pre_map[crs] =[]

            res.append(crs)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return res

        