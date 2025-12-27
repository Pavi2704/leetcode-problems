class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        arr=[]
        ans=[]
        for i in matrix:
            arr.append(min(i))
        for i in range(len(matrix[0])):
            a=0
            for j in range(len(matrix)):
                a=max(a,matrix[j][i])
            ans.append(a)
        for i in arr:
            if i in ans:
                return [i]
        return []
