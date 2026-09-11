class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        def mapping(x):
            h = { code : 0 for code in range(ord('a'), ord('z')+1) }
            for c in x:
                h[ord(c)] += 1
            return tuple([ n for key, n in h.items() ])
        
        mapped_l = {s : mapping(s) for s in strs}
        tuples = set( mapped_l.values() )
        mapped_idx = { x : i for i,x in enumerate(tuples)}
        l = [ [] for i in range(len(tuples)) ]

        for s in strs:
            l[ mapped_idx[ mapped_l[s] ] ].append(s)
        return l