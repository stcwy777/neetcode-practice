from collections import defaultdict
class TimeMap:

    def __init__(self):
        self._map = defaultdict(dict)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self._map[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self._map or len(self._map[key]) == 0:
            return ""
        elif timestamp not in self._map[key]:
            times = list(self._map[key].keys())
            times.sort()
            l, r = 0, len(times) - 1
            if timestamp < times[l]:
                return ""
            else:
                while l <= r:
                    m = (r - l) // 2 + l
                    if times[m] > timestamp:
                        r = m - 1
                    else:
                        l = m + 1
                return self._map[key][times[r]]
        else:
            return self._map[key][timestamp]
