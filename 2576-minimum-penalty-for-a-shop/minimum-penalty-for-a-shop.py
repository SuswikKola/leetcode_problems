class Solution:
    def bestClosingTime(self, customers: str) -> int:
        pref = []
        pref.append(customers.count("N"))
        for i in range(len(customers)-1,-1,-1):
            if customers[i]=="N":
                pref.append(pref[-1]-1)
            else:
                pref.append(pref[-1]+1)
        res = pref[::-1]
        m = min(res)
        return res.index(m)


