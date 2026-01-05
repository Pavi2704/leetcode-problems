class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        a = {}
        count = 0
        for d in dominoes:
            key = tuple(sorted(d))
            if key in a:
                count += a[key]
                a[key] += 1
            else:
                a[key] = 1
        return count
