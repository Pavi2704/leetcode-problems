class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        arr=[]
        for i in range(1,n+1):
            arr.append(i)
        b=list(combinations(arr,k))
        return b
        

        