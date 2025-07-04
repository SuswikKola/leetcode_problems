class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        lens = [1]
        for i in operations:
            lens.append(lens[-1]*2)
        shifting = 0
        for i in reversed(range(len(operations))):
            curr = lens[i]
            if k>curr:
                k-=curr
                if operations[i]==1:
                    shifting+=1
        return chr(ord('a')+(shifting%26))