#Day28 Special Calculator
from collections import deque

def min_steps(A, B):
    queue = deque([(A, 0)])
    visited = set([A])
    
    while queue:
        num, steps = queue.popleft()
        
        if num == B:  
            return steps
        
        for nxt in [num + 3, num - 2]:
            if 1 <= nxt <= 100 and nxt not in visited:  
                visited.add(nxt)
                queue.append((nxt, steps + 1))
    
    return -1  
A, B = map(int, input().split())
print(min_steps(A, B))
