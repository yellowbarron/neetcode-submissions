class Solution:
    def canJump(self, nums: List[int]) -> bool:
        stk= [(nums[0],0)]

        while stk:
            max_step = float('-inf')
            temp = []
            n, idx = stk.pop()
            if idx == len(nums)-1:
                return True
            for i in range(n):
                position = i + idx + 1
                if position < len(nums) and nums[position]+(position) > max_step:
                    max_step = nums[position]+(position)
                    temp = (nums[position],position)
            if temp:
                stk.append(temp)

        
        return False



        

        