class Solution:
    def isValid(self, s: str) -> bool:
        
        l = []
        opens = ['(','{','[']
        closes = [')','}',']']
        
        for c in s:
            if c in opens :
                i = opens.index(c)
                l.append(i)
            
            else:
                i = closes.index(c) 
                if len(l) == 0 or i != l.pop() :
                    return False
        return len(l) == 0