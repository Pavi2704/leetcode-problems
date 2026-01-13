class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:

        arr.sort()
        minimum=float("inf")
        ans=[]
        for i in range(len(arr)-1):
            diff=arr[i+1]-arr[i]
            minimum=min(minimum,diff)
        for i in range(len(arr)-1):
            if arr[i + 1] - arr[i] == minimum:
                ans.append([arr[i], arr[i + 1]])  
        return ans
            
        