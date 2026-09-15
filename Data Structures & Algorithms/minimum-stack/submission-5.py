class MinStack:
    from collections import Counter
    def __init__(self):
        self.min = None
        self.s = []
        self.c = Counter(self.s)

    def push(self, val: int) -> None:
        self.s.append(val)
        self.c[val] = 1 + self.c.get(val,0)
        self.min = min(val,self.min) if self.min is not None else val

    def pop(self) -> None:
        popped = self.s.pop()
        self.c[popped] -= 1
        if self.c[popped] == 0:
            del self.c[popped]
            self.min = min(self.c.keys()) if len(self.c.keys()) > 0 else None

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.min