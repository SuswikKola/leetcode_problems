class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        t = 0
        for i, x in enumerate(tickets):
            if i <= k:
                t += min(tickets[i], tickets[k])
            else:
                t += min(tickets[i], tickets[k] - 1)

        return t