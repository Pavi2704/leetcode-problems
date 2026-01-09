class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        arr = []
        ans = []
        for idx in range(len(s)):
            if s[idx] == c:
                arr.append(idx)
        for i in range(len(s)):
            nearest = min(abs(i - j) for j in arr)
            ans.append(nearest)
        
        return ans
