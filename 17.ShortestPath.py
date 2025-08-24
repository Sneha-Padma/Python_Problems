# Day17 Shortest Path in a Graph
import heapq
import sys
def dijkstra(n, graph, s, t):
    dist = [float('inf')] * (n + 1)
    dist[s] = 0
    pq = [(0, s)]  
    
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))
    
    return dist[t] if dist[t] != float('inf') else -1

n, m, s, t = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))
print(dijkstra(n, graph, s, t))
