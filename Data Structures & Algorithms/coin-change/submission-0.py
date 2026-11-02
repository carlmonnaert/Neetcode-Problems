class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # res[i] is the number of coins needed to make amount i
        # res[i+1] = min(res[n+1-c] + c for c in coins)
        res = [ 1 if i in coins else -1 for i in range(amount+1) ]
        res[0] = 0
        for i in range(amount+1):
            counts_list = [ res[i-c] + 1 for c in coins if 0 <= i-c and res[i-c] != -1]
            res[i] = res[i] if len(counts_list) == 0 else min(counts_list)
        return res[-1]