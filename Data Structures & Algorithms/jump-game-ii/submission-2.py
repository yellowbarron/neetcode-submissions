class Solution:
    def jump(self, nums: List[int]) -> int:
         stk= [(nums[0],0)]
         cnt = 0
         
         if len(nums)==1:
            return 0
         while stk:
            max_step = float('-inf')
            temp = []
            n, idx = stk.pop()
            cnt +=1 
            if (idx +n )  >= len(nums)-1:
                return cnt
            for i in range(n):
                position = i + idx + 1
                if position < len(nums) and nums[position]+(position) > max_step:
                    max_step = nums[position]+(position)
                    temp = (nums[position],position)
            if temp:
                stk.append(temp)
                

        
         return cnt