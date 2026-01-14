class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        arr=[]
        for i in range(left,right+1):
            if '0' in str(i):
                continue
            a=True
            for j in str(i):
                if i % int(j)!=0:
                    a=False
                    break
            if a:
                arr.append(i)
        return arr
            