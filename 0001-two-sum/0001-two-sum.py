class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hasMap={}
        for i , n in enumerate (nums):
            diff = target -n
            if diff in hasMap:
                return [hasMap[diff],i]
            hasMap[n]=i
        return