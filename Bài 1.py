# Code By Lê Văn Long
import heapq

INF = int(1e9)

def dijkstra(n, adj):
    d = [INF] * (n + 1)
    d[1] = 0  
    Q = []
    heapq.heappush(Q, (0, 1))
    
    while Q:
        kc, u = heapq.heappop(Q)
        if kc > d[u]:
            continue
        for v, w in adj[u]:
            if d[v] > d[u] + w:
                d[v] = d[u] + w
                heapq.heappush(Q, (d[v], v))
    
    return d[1:]

if __name__ == "__main__":
    n, m = map(int, input().split())
    adj = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        a, b, c = map(int, input().split())
        adj[a].append((b, c))

    result = dijkstra(n, adj)
    print(" ".join(map(str, result)))
