class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        ans=0
        i=0
        j=1
        while j<len(nums):
            a=nums[i:j]
            b=nums[j:]
            c=sum(a)+sum(b)
            if c%2==0:
                ans+=1
            j+=1
        return ans