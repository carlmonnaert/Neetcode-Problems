class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i,t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                t_stack , i_stack = stack.pop()
                res[i_stack] = i - i_stack
            stack.append([t,i])
        return res