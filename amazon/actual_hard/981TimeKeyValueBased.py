class TimeMap:

    def __init__(self):
        self.key_time_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_time_map[key].append([timestamp, value])
        

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.key_time_map:
            return ""
        
        if timestamp < self.key_time_map[key][0][0]:
            return ""

        l, r = 0, len(self.key_time_map[key])
        while l < r:
            m = (l + r) // 2
            if self.key_time_map[key][m][0] <= timestamp:
                l = m + 1
            else:
                r = m
        return "" if r == 0 else self.key_time_map[key][r - 1][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)