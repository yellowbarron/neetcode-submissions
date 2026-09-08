class Solution:
    def climbStairs(self, n: int) -> int:
        combo = 0
        def crazydfs(n1,n2, combo):
            if n2 ==0:
                combo+=1 
                return combo
            

            c =  math.factorial(n1+n2)//(math.factorial(n1)*math.factorial(n2))
            combo += c 
            return crazydfs(n1+2,n2-1,combo)
    

        n2 = n//2
        n1 = n - (n//2)*2

        combo = crazydfs(n1,n2,0)

        return combo 

