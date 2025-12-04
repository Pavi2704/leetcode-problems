class Solution:
    def sortString(self, s: str) -> str:
        freq=Counter(s)
        ans=[]
        while len(ans)<len(s):
            for ch in sorted(freq):
                if freq[ch]>0:
                    ans.append(ch)
                    freq[ch]-=1
            for ch in sorted(freq,reverse=True):
                if freq[ch]>0:
                    ans.append(ch)
                    freq[ch]-=1
        return "".join(ans)


