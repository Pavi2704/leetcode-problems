class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minn=nums[0]
        maxx=nums[0]
        ans=nums[0]
        for i in range(1,len(nums)):
            if nums[i]<0:
                minn,maxx=maxx,minn
            minn=min(nums[i],minn*nums[i])
            maxx=max(nums[i],maxx*nums[i])
            ans=max(ans,maxx)
        return ans
        