class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        h = ((hour%12)+(minutes/60))*5
        a = abs(minutes-h)
        res = a*(360/60)
        return min(360-res,res)