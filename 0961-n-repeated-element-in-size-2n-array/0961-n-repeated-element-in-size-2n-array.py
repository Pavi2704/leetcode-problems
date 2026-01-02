class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        nums.sort()
        for i in nums:
            if nums.count(i)>1:
                b=max(0,i)
                
        return b

        