class TimeMap:

    def __init__(self):
        self.dic = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic.setdefault(key,[]).append([timestamp, value])
            

    def get(self, key: str, timestamp: int) -> str:
        data = self.dic.get(key, [])
        l, r = 0, len(data) - 1
        id_ts = None

        while l <= r:
            p = (l + r) // 2
            ts_p = data[p][0]
            
            if ts_p < timestamp:
                id_ts = p
                l = p + 1
    
            elif ts_p == timestamp:
                id_ts = p
                break
            
            else:
                r = p - 1

        if id_ts is not None:
            return self.dic[key][id_ts][1]

        return ""