class LRUCache:

    def __init__(self, capacity: int):
        self._cap = capacity
        self._map = {}     
        self._cache = deque([])   

    def get(self, key: int) -> int:
        if key in self._map:
            self._cache.remove(key)
            self._cache.append(key)
            return self._map[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self._map:
            self._map[key] = value
            self._cache.remove(key)
            self._cache.append(key)            
        else:
            if self._cap > 0:
                self._cap -= 1
            else:
                least_visited = self._cache.popleft()
                del self._map[least_visited]
            self._map[key] = value
            self._cache.append(key) 
