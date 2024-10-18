# Code By Lê Văn Long - B22DCVT316
import heapq

INF = int(1e18)

def dijkstra(n, adj, k):
    d = [[] for _ in range(n + 1)]
    d[1].append(0)
    Q = []
    heapq.heappush(Q, (0, 1))
    
    while Q:
        kc, u = heapq.heappop(Q)
        if len(d[u]) > k:
            continue
        for v, w in adj[u]:
            new_cost = kc + w
            if len(d[v]) < k:
                heapq.heappush(Q, (new_cost, v))
                d[v].append(new_cost)
                d[v].sort()
    
    return d[n][:k]

if __name__ == "__main__":
    n, m, k = map(int, input().split())
    adj = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        a, b, c = map(int, input().split())
        adj[a].append((b, c))

    result = dijkstra(n, adj, k)
    print(" ".join(map(str, result)))
