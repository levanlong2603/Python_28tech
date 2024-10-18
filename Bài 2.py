# Code By Lê Văn Long
import heapq

INF = int(1e9)

def dijkstra(n, adj):
    d = [[INF, INF] for _ in range(n + 1)]
    d[1][0] = 0
    Q = []
    heapq.heappush(Q, (0, 1, 0))
    
    while Q:
        kc, u, used = heapq.heappop(Q)
        if kc > d[u][used]:
            continue
        for v, w in adj[u]:
            if d[v][used] > d[u][used] + w:
                d[v][used] = d[u][used] + w
                heapq.heappush(Q, (d[v][used], v, used))
            if used == 0 and d[v][1] > d[u][0] + w // 2:
                d[v][1] = d[u][0] + w // 2
                heapq.heappush(Q, (d[v][1], v, 1))
    
    return min(d[n])

if __name__ == "__main__":
    n, m = map(int, input().split())
    adj = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        a, b, c = map(int, input().split())
        adj[a].append((b, c))

    result = dijkstra(n, adj)
    print(result)
