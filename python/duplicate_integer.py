class Solution:
    # https://neetcode.io/problems/duplicate-integer/question
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 0: return False
        keep = {}
        for i in nums:
            if i in keep:
                return True
            keep[i] = 'random'
            
        return False
