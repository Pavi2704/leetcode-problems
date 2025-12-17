class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        arr=[]
        ans=[]
        for i,j in points:
            arr.append(i)
        arr.sort()
        for i in range(len(arr)-1):
            ans.append(abs(arr[i]-arr[i+1]))
        return max(ans)
