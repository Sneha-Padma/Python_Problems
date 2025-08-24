#Day 22 Design and Simulate an LRU Cache
from collections import OrderedDict
class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
          
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            
            self.cache.popitem(last=False)

if __name__ == "__main__":
    C, Q = map(int, input().split())
    lru = LRUCache(C)

    for _ in range(Q):
        query = input().split()
        if query[0] == "GET":
            key = int(query[1])
            print(lru.get(key))
        elif query[0] == "PUT":
            key, value = int(query[1]), int(query[2])
            lru.put(key, value)
