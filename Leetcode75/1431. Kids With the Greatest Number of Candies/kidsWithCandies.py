class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m = max(candies) - extraCandies
        result = []
        for i in candies:
            if i >= m:
                result.append(True)
            else:
                result.append(False)
        return result
