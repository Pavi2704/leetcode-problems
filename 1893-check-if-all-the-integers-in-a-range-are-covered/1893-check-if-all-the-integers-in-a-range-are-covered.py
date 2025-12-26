class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        a=[]
        for i in ranges:
            a+=range(i[0],i[-1]+1)
        for i in range(left,right+1):
            if i not in a:
                return False
        return True
        