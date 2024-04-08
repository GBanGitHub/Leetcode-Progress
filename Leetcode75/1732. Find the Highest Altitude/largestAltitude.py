class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxVal = 0
        alt = 0
        for i in gain:
            alt += i
            maxVal =  max(alt,maxVal)
        return maxVal
