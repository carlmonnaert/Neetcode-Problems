class Solution:

    def encode(self, strs: List[str]) -> str:
        
        def aux(c):
            code = str(ord(c))
            to_add = 3 - len(code)
            for i in range(to_add):
                code = '0' + code
            return code
        
        code = ""
        for s in strs:
            for c in s:
                code = code + aux(c)
            code = code + "sss"
        return code

    def decode(self, s: str) -> List[str]:
        l = []
        x = ""
        for i in range(0, len(s) - 2, 3):
            sub = s[i:i+3]
            
            if sub != "sss":
                x = x + chr(int(sub))
            
            else:
                l.append(x)
                x = ""
        return l