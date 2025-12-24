class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort(reverse=True)
        a=sum(apple)
        count=0
        b=0
        for i in capacity:
            b+=i
            count+=1
            if b>=a:
                return count
