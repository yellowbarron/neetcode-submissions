class Solution:
    def rob(self, nums: List[int]) -> int:
        stk = []
        if len(nums) < 2:
            return nums[0]


        for i in range(len(nums)):
            if len(stk) < 2:
                stk. append(nums[i])
            elif len(stk)==2:
                stk.append(nums[i]+stk[-2])
            else:
                stk.append(nums[i]+max(stk[-2],stk[-3]))
            
        
        
        return max(stk[-1],stk[-2])
        