class Solution:
    def perform(self,t,e1,e2):
            if t =='+':
                return e1 + e2
            elif t =='-':
                return e1 - e2
            elif t =='*':
                return e1 * e2
            elif t =='/':
                return e1 / e2

    def evalRPN(self, tokens: List[str]) -> int:
        ops = ['+', '-', '/', '*']
        def pop(e):
            t = e.pop()
            if t not in ops:
                return int(t)
            else:
                e2, e1 = pop(e), pop(e)
                return int(self.perform(t,e1,e2))
        return pop(tokens)

