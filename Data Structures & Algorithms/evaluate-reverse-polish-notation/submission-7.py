class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = '+-/*'
        s = []
        for t in tokens:
            
            if t in ops:
                b = s.pop()
                a = s.pop()

                if t == '+':
                    s.append(a + b)

                elif t == '-':
                    s.append(a - b)

                elif t == '*':
                    s.append(a * b)

                elif t == '/':
                    s.append(int(a / b))
            else:
                s.append(int(t))
        return s[0]

