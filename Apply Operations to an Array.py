class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
       
        i = 0
        while i < len(nums) - 1:  
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
            i += 1
        ans =[]
        for i in nums:
            if i != 0 :
                ans.append(i)
        for i in nums:
            if i == 0 :
                ans.append(i)
        
        return ans
