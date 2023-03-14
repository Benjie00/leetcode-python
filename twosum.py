class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        nums_key = {}
        
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in nums_key:
                return [nums_key[complement], i]
            nums_key[nums[i]] = i
    
            