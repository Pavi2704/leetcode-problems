class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        a=sorted(nums[1:])
        b=nums[0]+a[0]+a[1]
        return b
        